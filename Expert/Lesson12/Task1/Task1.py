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
            raise AttributeError(f'Свойство "{self.param_name}" должно быть строкой')
        elif not (str(value).isalpha or str(value).istitle):
            raise AttributeError("ФИО должно состоять только из букв и начинаться с заглавной буквы")

class Student:
    name = Name()
    subjects = dict()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.load_subjects(subjects_file);
    
    def load_subjects(self, subjects_file):
        result = dict()

        with open(subjects_file, "r", encoding="utf-8") as f:        
            csv_reader = csv.reader(f, delimiter=',')
            result = {item:0 for item in list(*[col for col in [row for row in csv_reader]])}
        
        return result

    #def __str__(self):
    #    return f"{super(MyStr, self).__str__()} (Автор: {self.author}, Время создания: {self.time.strftime('%Y-%m-%d %H:%M')})"

if __name__ == "__main__": 
    student = Student('Иванов Петя', 'subjects.csv')
    print(student)