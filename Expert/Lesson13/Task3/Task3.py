#Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). 
#Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
#Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). 
#Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
class InvalidError(Exception):
    pass

class InvalidNameError(InvalidError):
    pass

class InvalidAgeError(InvalidError):
    pass

class InvalidIdError(InvalidError):
    pass

class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)


class RangeText(Range):
    def validate(self, value):
        if not isinstance(value, str):
            raise InvalidNameError(f'свойство "{self.param_name}" должно быть строкой')
        elif value is None or value == str():
            raise InvalidNameError(f'Invalid name: . Name should be a non-empty string.')


class RangeNumeric(Range):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        if not isinstance(value, int):
            raise InvalidError(f'property "{self.param_name}" must be a number')
        elif self.min_value is not None and value < self.min_value and self.param_name == "_Age":
            raise InvalidAgeError(f'Invalid age: {value}. Age should be a positive integer.')
        elif self.max_value is not None and value < self.min_value and self.param_name == "_ID":
            raise InvalidIdError(f'Invalid id: {value}. Id should be a 6-digit positive integer between {self.min_value} and {self.max_value}.')            
        elif self.max_value is not None and value > self.max_value and self.param_name == "_ID":
            raise InvalidIdError(f'Invalid id: {value}. Id should be a 6-digit positive integer between {self.min_value} and {self.max_value}.')            

class Person:
    LastName = RangeText()
    FirstName = RangeText()
    MiddleName = RangeText() 

    Age = RangeNumeric(0, 100)

    def __init__(self, LastName, FirstName, MiddleName, Age):
        self.LastName = LastName
        self.FirstName = FirstName
        self.MiddleName = MiddleName

        self.Age = Age

    def birthday(self):
        self.Age += 1

    def get_age(self):
        return self.Age

class Employee(Person):
    ID = RangeNumeric(100000, 999999)

    def __init__(self, LastName, FirstName, MiddleName, Age, ID):
        super().__init__(LastName, FirstName, MiddleName, Age)
    
        self.ID = ID
    
    def get_level(self):
        ###уровень сотрудника###                
        return sum(map(int, str(self.ID))) % 7

if __name__ == "__main__":
    employee = Employee("Bob", "Johnson", "Brown", 40, 12345)