#Разработайте программу для работы с прямоугольниками. 
#Необходимо создать класс Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
#Атрибуты класса:
#width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
class Rectangle:
    '''
    Класс Rectangle, представляет прямоугольник с заданными шириной и высотой.
    '''
    def __init__(self, width: int, height: int = None):
        self.width = width
        self.height = width if height is None else height

    def perimeter(self): 
        '''Метод для вычисления периметра прямоугольника. Возвращает целое число - значение периметра.'''
        return 2 * (self.width + self.height)

    def area(self): 
        '''Метод для вычисления площади прямоугольника. Возвращает целое число - значение площади.'''
        return self.width * self.height

    def __add__(self, other):
        '''Магический метод, который определяет операцию сложения (+)'''
        return Rectangle(self.width + other.width, self.height + other.height)

    def __sub__(self, other): 
        '''Магический метод, который определяет операцию вычитания (-)'''
        return Rectangle(abs(self.width - other.width), abs(self.height - other.height))
        #return Rectangle(abs(self.perimeter() - other.perimeter()) / 2 - other.width if other.width < other.height else other.height, other.width if other.width > other.height else other.height)

    def __lt__(self, other): 
        '''Магический метод, который определяет операцию "меньше" (<)'''
        return self.area() < other.area()

    def __eq__(self, other): 
        '''Магический метод, который определяет операцию "равно" (==)'''
        return self.area() == other.area()

    def __le__(self, other): 
        '''Магический метод, который определяет операцию "меньше или равно" (<=)'''
        return self.area() <= other.area()

    def __str__(self): 
        '''Магический метод, возвращающий строковое представление прямоугольника'''
        return f'Прямоугольник со сторонами {self.width} и {self.height}'
    
    def __repr__(self): 
        '''Магический метод, возвращающий строковое представление прямоугольника'''
        return f'Rectangle({self.width}, {self.height})'

if __name__ == "__main__":
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 3)

    print(rect1)
    print(rect2)

    print(rect1.perimeter())
    print(rect1.area())
    print(rect2.perimeter())
    print(rect2.area())

    rect_sum = rect1 + rect2
    rect_diff = rect1 - rect2

    print(rect_sum)
    print(rect_diff)

    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)

    print(repr(rect1))
    print(repr(rect2))