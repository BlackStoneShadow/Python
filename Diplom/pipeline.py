import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import pickle

from typing import Callable
from math import ceil
from pylab import rcParams
from scipy import stats
from scipy.stats.mstats import winsorize
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import roc_auc_score, f1_score
from inspect import getfullargspec

class DataFrame(pd.DataFrame):
    """расширение DataFrame"""
    @property    
    def columns_num(self):
        """количественные признаки"""
        return self[self.columns.tolist()].select_dtypes(include=['uint8', 'int32', 'int64', 'float32', 'float64']).columns.tolist()
        
    @property    
    def column_cat(self):
        """номинативные признаки"""
        return self[self.columns.tolist()].select_dtypes(include=['object', 'category']).columns.tolist()                                  
    
    def columns_except(self, columns, excepts):
        return self[[item for item in columns if item not in excepts]]
    
class DataPipeline:     
    def __init__(self, **kwargs):
        """Инициализация класса"""                       
        # уровень стат значимости
        self.alpha = 0.05
        # срнднйи уровень корреляции
        self.corr = 0.7
        # объясненная дисперсия компонента
        self.varatio = 0.8
        # пороговое значение в три сигмы
        self.threashold = 3    
        # пропорции деления набора
        self.test_size = 0.33
        # кодировщики
        self.__encoders__ = dict()        
        
        # параметры класса
        for key, value in kwargs.items():
            setattr(self, f"__{key}__", value)    
            
        assert self.__target__ is not None                  
        assert self.__features__ is not None                  
        assert self.__train_data__ is not None            
        
        # подготовка обучения            
        self.__train_data__  = self.prepare(self.__train_data__)        

    def __getstate__(self) -> dict:
        state = dict()    

        state["encoders"] = self.__encoders__
        state["model"] = self.__model__
        state["features"] = self.__features__
        state["target"] = self.__target__        
        
        return state
    
    def __setstate__(self, state: dict):            
        self.__encoders__ = state["encoders"]
        self.__model__ = state["model"]
        self.__features__ = state["features"]
        self.__target__ = state["target"]

    def prepare(self, data):
        data = DataFrame(data[self.__features__ + [self.__target__]])
        data = DataFrame(data[~data[self.__target__].isna()])                    

        return data
    
    def sc_data(func: Callable):
        """Декоратор стандартизации"""
        def wrapper(self, data):                     
            # стандартизация обучения                    
            self.__sc_train_data__ = func(self, data)                                    
            # исключение целевой переменной из количественных признаков            
            column = self.__sc_train_data__.columns_except(self.__sc_train_data__.columns_num, self.__target__).columns
            # создаем стандартизатор
            if "scaler" not in self.__encoders__:
                self.__encoders__["scaler"] = StandardScaler()        
                self.__encoders__["scaler"].fit(self.__sc_train_data__[column])                           
            # стандартизация признаков                                     
            self.__sc_train_data__ = DataFrame(pd.concat([DataFrame(self.__encoders__["scaler"].transform(self.__sc_train_data__[column]), columns=column, index=self.__sc_train_data__.index),\
                                                     self.__sc_train_data__[self.__sc_train_data__.column_cat]], axis=1))                        
            #print("train resize")
            # понижение размерности                   
            #self.sc_train_data = DataFrame(self._resize_(self.sc_train_data))                                            
            
        return wrapper    
    
    @sc_data
    def transform(self, data):       
        """Трансформация данных"""   
        data[self.__target__] = data[self.__target__].astype("category")
        # заменяем inf на nan тогда моедль сможет их предсказать
        data.replace([np.inf, -np.inf], np.nan, inplace = True)
        
        # обработка количественных признаков    
        for item in data.columns_num:            
            data = self._transform_num_(data, item)                                                                                     
                
        # обработка текстовых признаков
        for item in data.column_cat:                   
            data = self._transform_vec_(data, item)
        
        # обработка номинальных признаков
        for item in data.column_cat:                   
            data = self._transform_cat_(data, item)                    
        
        return data

    def _transform_vec_(self, data, column):        
        """Векторизация текстовых признаков"""                         
        if column in self.__features__:        
            data[column] = data[column].fillna(data[column].mode()[0])                    
            
            if column not in self.__encoders__:                
                self.__encoders__[column] = TfidfVectorizer()        
                self.__encoders__[column].fit(data[column])                            
                
            # векторизация текстового признака
            vect = self.__encoders__[column].transform(data[column])                                        
            data = DataFrame(pd.concat([data.columns_except(data.columns, column),\
                                       DataFrame(vect.todense(), columns=self.__encoders__[column].get_feature_names_out(), index=data.index)], axis=1))            
            
        return data            

    def _transform_cat_(self, data, column):
        """Трансформация номинальных признаков"""                         
        # заменяем пропуски модой                                   
        data[column] = data[column].fillna(data[column].mode()[0])                    
        # создаем кодировщик
        if column not in self.__encoders__:
            self.__encoders__[column] = LabelEncoder()        
            self.__encoders__[column].fit(data[column])                    
        # кодируем признак                         
        data[column] = self.__encoders__[column].transform(data[column])                    
        # возвращаем тип признака из числового после кодирования
        data[column] = data[column].astype("category")
        
        return data        
        
    def _transform_num_(self, data, column):        
        """Трансформация количественных признаков"""        
        if len(data) == 1:
            return data
        # пробуем предсказать пропуски                        
        cdata = DataFrame(data.copy()) 
        # запомнинание пропусков        
        cdata['isna'] = np.where(cdata[column].isna(), True, False)                                             
        # заполнение пропусков в копии, т.к моедель не работает с ними
        for item in cdata.column_cat:            
            if cdata[item].isna().values.any():
                cdata[item] = cdata.fillna(cdata[item].mode())        
        for item in cdata.columns_num:
            if cdata[item].isna().values.any():
                cdata[item] = cdata.fillna(cdata[item].mean())                   
        # предсказание пропусков если можно сформировать обучающий и тестовый набор
        if True in cdata['isna'].values and False in cdata['isna'].values:
            # используем простую модель
            model = LinearRegression()
            # формируем тестовый и обучающий набор
            X_test = cdata.columns_except(cdata.columns, column)[cdata['isna']==True]
            X_train = cdata.columns_except(cdata.columns, column)[cdata['isna']==False]
            y_train = cdata[cdata['isna']==False][column]                    
            # обучение модели
            model.fit(X_train, y_train)
            # выполняем предсказание пропущенного прзнака        
            data.loc[cdata['isna'], [column]] = model.predict(X_test)                                      
        
        # очень странно, если не трогать целевую переменную или выполнить её винсоризацию,
        # то результат обучения модели существенно лучше, хотя мат статистика по ней хуже чем после zscore?
        # bins по целевой переменной решает проблему статистики, но предсказание модели теперь имеют погрешность бина
        if column == self.__target__:            
            data[column] = winsorize(data[column], limits=[0.1, 0.1])                                                            
        
        # обработка выбрасов, вычисляем z-Score в цикле пока не подавим их все       
        while column != self.__target__:            
            z = np.abs(stats.zscore(data[column]))                                                     
            if not z[z > self.threashold].any():
                break            
            # среднее если данные имеют нормальное распределение, иначе медиана                                    
            if stats.shapiro(data[column].values.reshape(-1))[1] > self.alpha:                        
                data.loc[z > self.threashold, column] = data[column].mean()            
            else:            
                data.loc[z > self.threashold, column] = data[column].median()                                                          
        
        return data          
    
    def _resize_(self, data, level = 0):
        """понижение размерности"""           
        m_corr, level = data.corr(), level + 1        
        for item in m_corr.columns:            
            # поиск взаимокорреляции признаков по матрице
            column = list(m_corr[m_corr[item] > self.corr].index)
            # корреляция не с самим собой и не одни компоненты 
            if len(column) > 1 and not all('component' in item for item in column):
                dim_reducer = PCA(n_components=1, random_state=42)                
                components = dim_reducer.fit_transform(data[column])                            
                # уровень дисперсии достаточен для свертывания
                if dim_reducer.explained_variance_ratio_ >= self.varatio:
                    data = DataFrame(pd.concat([data.drop(column, axis=1),\
                                                pd.DataFrame(data = components, columns = [f'component_{level}'])], axis=1))                                                                                                
                    # результат свертки
                    print(f'{column} -> component_{level} var:{dim_reducer.explained_variance_ratio_}')
                    # рекурсивный поиск компонент
                    return self._resize_(data, level)               
        return data     

    @property
    def train_data(self):
        return DataFrame(self.__train_data__)
        
    @property
    def sc_train_data(self):
        return DataFrame(self.__sc_train_data__)

    @property
    def encoders(self):
        return self.__encoders__          
    
    @property
    def model(self):
        return self.__model__        
    
    def split(self, X, y):
        """Разделение набора"""             
        return train_test_split(X, y, test_size=self.test_size, random_state=42)
    
    def search_param(self, data):
        """Поиск гиперпараметров"""        
        params = {
            'criterion': ['squared_error', 'absolute_error', 'friedman_mse', 'poisson', 'gini', 'entropy'],
            'n_estimators': [item for item in range(10, 100, 10)],            
            'max_depth': [item for item in range(1, 10, 2)],
            'max_features': [item for item in range(1, 10, 2)],
            'min_samples_leaf': [item for item in range(1, 10, 2)],
        }

        clf = GridSearchCV(
            estimator=RandomForestClassifier(random_state=42),
            param_grid=params,            
            scoring='roc_auc',
            n_jobs=-1,
            cv=5
        )              
        # формируем X и y из обучающего набора
        X_train, X_valid, y_train, y_valid = self.split(self.__sc_train_data__, self.__train_data__ [self.__target__])
        # искать праметры лучше на всеъ данных
        clf.fit(pd.concat([X_train, X_valid]), pd.concat([y_train, y_valid]))
        
        return clf.best_params_
    
    def fit(self, model, data):
        """Обучение модели"""                     
        self.__model__ = model
        # разделение набора на обучающий и проверочный
        X_train, X_valid, y_train, y_valid = self.split(data.columns_except(data.columns, self.__target__), data[self.__target__])
        
        self.__model__.fit(X_train, y_train)                        
        
        return self.__model__
        
    def predict(self, model, data):
        """Предсказание зависимой переменной"""        
        return model.predict(data.columns_except(data.columns, self.__target__))    
    
    def importances(self, model, data):
        """оценка признаков модели"""                                
        return pd.DataFrame(zip(data.columns_except(data.columns, self.__target__).columns, model.feature_importances_),\
                            columns = ['name', 'value']).sort_values(by = 'value', ascending = False)                          
    
    def scatterplot(self, model, data):
        """график scatterplot качесива модели"""    
        X_train, X_valid, y_train, y_valid = self.split(data.columns_except(data.columns, self.__target__), data[self.__target__])

        y_pred = self.predict(model, DataFrame(X_train))    
        
        plt.subplot(121)
        plt.xlabel('Predicted values')
        plt.ylabel('True values')                
        plt.title(f"train f1:{round(f1_score(y_train, y_pred, average='micro'), 3)}")        
        sns.scatterplot(x = y_train, y = y_pred)
        
        y_pred = self.predict(model, DataFrame(X_valid))        
        
        plt.subplot(122)
        plt.xlabel('Predicted values')
        plt.ylabel('True values')                
        plt.title(f"valid f1:{round(f1_score(y_valid, y_pred, average='micro'), 3)}")        
        sns.scatterplot(x = y_valid, y = y_pred)

        plt.show()                      

    def boxplot(self, data):
        """график box-plot"""                           
        data.boxplot(column = data.columns_num, grid = False, rot = 45)
        
    def corrplot(self, data):
        """график корреляции"""              
        plt.title('Корреляционная матрица')
        sns.heatmap(data.corr(), annot = True)
        plt.show()