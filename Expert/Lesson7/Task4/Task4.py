#✔ Создайте функцию, которая создаёт файлы с указанным расширением.
#Функция принимает следующие параметры:
#✔ расширение
#✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
#✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
#✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
#✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
#✔ количество файлов, по умолчанию 42
#✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from sys import path
#For absolute import, support if __name__ == "__main__"
path.append('../')
#Absolute package import
from module import shfutil
from sys import argv

if len(argv) == 7:
    if shfutil.generator(argv[1], int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]), int(argv[6])):
        print("Sucess complited!")
    else:
        print("Error operation!")
else:
    print(help(shfutil.generator))