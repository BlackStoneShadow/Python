import io
import pickle
import pandas as pd

from chardet import detect
from flask import Flask, jsonify, request
from flask_cors import CORS
from pipeline import DataFrame, DataPipeline

app = Flask(__name__)
# загрузка конвейеров моделей
with open("pipelines.pkl", "rb") as f:
    pipelines = pickle.load(f)    

CORS(app, resources={'/pipeline':{"origins":"http://localhost:8080"}})

@app.route('/pipeline', methods=['POST'])
def post_request_all():    
    try:
        assert request.data, "no data"
        assert detect(request.data)["encoding"] == "utf-8", "code page not utf-8"                
        
        result = dict()    
        for target, image in pipelines.items():                           
            file = io.BytesIO(image)            
            # загрузка конвейера
            pipeline = Unpickler(file).load()
            #pipeline = pickle.loads(image)
            # обученный кодировщик
            encoder = pipeline.encoders[target]                    
            # загрузка параметров запроса
            data = DataFrame(pd.DataFrame(pd.read_json(request.data.decode("utf-8"), typ='series')).transpose())
            # модель требует определение всех признаков при подготовки данных, пишем любое значение
            data[target] = encoder.classes_[0]
            # подготовка признаков
            pipeline.transform(pipeline.prepare(data))            
            # предсказание целевой переменной
            result[target] = str().join(encoder.inverse_transform(pipeline.predict(pipeline.model, pipeline.sc_train_data)))
            # результат
        return jsonify({'result': result})
    except AssertionError as error:
        return jsonify({'result': error.args})
    except Exception as error:        
        return jsonify({'result': error.msg if hasattr(error, "msg") else error.args})

# Обеспечивает нахождение класса при загрузки из pickle в Docker
class Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__":
            module = "pipeline"
            
        return super().find_class(module, name)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)