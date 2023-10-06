#Напишите следующие функции:
#○ Нахождение корней квадратного уравнения
#○ Генерация csv файла с тремя случайными числами в каждой строке.
#100-1000 строк.
#○ Декоратор, запускающий функцию нахождения корней квадратного
#уравнения с каждой тройкой чисел из csv файла.
#○ Декоратор, сохраняющий переданные параметры и результаты работы
#функции в json файл.
from sys import path
#For absolute import, support if __name__ == "__main__"
path.append('../')
#Absolute package import
from module import shfutil
from sys import argv

if len(argv) == 2:
    if shfutil.run(int(argv[1])):
        print("Sucess complited!")
    else:
        print("Error operation!")
else:
    print(help(shfutil.run))