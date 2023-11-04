#Создайте класс студента.
#○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
#наличие только букв.
#○ Названия предметов должны загружаться из файла CSV при создании
#экземпляра. Другие предметы в экземпляре недопустимы.
#○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
#тестов (от 0 до 100).
#○ Также экземпляр должен сообщать средний балл по тестам для каждого
#предмета и по оценкам всех предметов вместе взятых. 
import csv

__GRADES__ = "grades"
__SCORES__ = "test_scores"

class Name:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):        
        if not isinstance(value, str):
            raise ValueError(f'Свойство "{self.param_name}" должно быть строкой')
        elif not (str(value).replace(" ", "").isalpha() and str(value).istitle()):
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")

class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f'свойство "{self.param_name}" должно быть целым числом')
        elif self.min_value is not None and value < self.min_value:
            raise ValueError(f"значение {value} должно быть больше или равно {self.min_value}")
        elif self.max_value is not None and value > self.max_value:
            raise ValueError(f"{'Оценка должна' if self.param_name == '__Student__grade' else 'Результат теста должен'} быть целым числом от {self.min_value} до {self.max_value}")

class Student:
    name = Name()
    subjects = dict()

    __grade = Range(2, 5)
    __test_scope = Range(0, 100)

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file);

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise ValueError(f"Предмет {name} не найден")

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def add_grade(self, subject, grade):
        if subject in self.subjects:
            self.__grade = grade
            self.subjects[subject]['grades'].append(grade)
        else:
            raise ValueError(f"Предмет {subject} не найден")

    def  add_test_score(self, subject, test_score):
        if subject in self.subjects:
            self.__test_scope = test_score
            self.subjects[subject]['test_scores'].append(test_score)
        else:
            raise ValueError(f"Предмет {subject} не найден")

    def get_average_grade(self):         
        return sum(sum(value[__GRADES__]) for key, value in self.subjects.items() if len(value[__GRADES__]) > 0) /\
               sum(len(value[__GRADES__]) for key, value in self.subjects.items() if len(value[__GRADES__]) > 0) 

    def get_average_test_score(self, subject):
        if subject in self.subjects:
            return sum(self.subjects[subject][__SCORES__]) / len(self.subjects[subject][__SCORES__])
        else:
            raise ValueError(f"Предмет {subject} не найден")
    
    def load_subjects(self, subjects_file):
        result = dict()

        with open(subjects_file, "r", encoding="utf-8") as f:        
            csv_reader = csv.reader(f, delimiter=",")            
            result = {item:{__GRADES__: [], __SCORES__: []} for item in [col for col in [row for row in csv_reader]][0]}
        
        return result

    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {", ".join(key for key, value in self.subjects.items() if len(value[__GRADES__]) > 0)}'

if __name__ == "__main__": 
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)