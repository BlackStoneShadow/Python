#Допишите в вашу задачу Archive обработку исключений.
#Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является строкой или является пустой строкой.
#И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом с плавающей запятой.
from typing import Union

class InvalidError(Exception):
    pass

class InvalidTextError(InvalidError):
    pass

class InvalidNumberError(InvalidError):
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
            raise InvalidTextError(f'свойство "{self.param_name}" должно быть строкой')
        elif value is None or value == str():
            raise InvalidTextError(f'Invalid text: . Text should be a non-empty string.')


class RangeNumeric(Range):
    def validate(self, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise InvalidNumberError(f'свойство "{self.param_name}" должно быть числом')
        elif value <= 0:
            raise InvalidNumberError(f'Invalid number: {value}. Number should be a positive integer or float.')

class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    text = RangeText()
    number = RangeNumeric()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

if __name__ == "__main__":
    arch1 = Archive('1', 1)
    print(arch1)

    arch2 = Archive('2', 2)
    print(arch2)