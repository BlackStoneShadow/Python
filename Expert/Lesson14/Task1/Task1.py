import doctest

class NegativeValueError(ValueError):
    pass


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        '''
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r2 = Rectangle(3, 4)
        >>> r2.width
        3
        >>> r2.height
        4
        >>> r4 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -2
        '''
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')

        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника

        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника

        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников

        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """        

        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width

        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного

        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"

if __name__ == "__main__":
    doctest.testmod(verbose=True)