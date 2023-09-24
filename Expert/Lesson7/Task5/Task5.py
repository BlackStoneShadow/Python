#✔ Доработаем предыдущую задачу.
#✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
#✔ Расширения и количество файлов функция принимает в качестве параметров.
#✔ Количество переданных расширений может быть любым.
#✔ Количество файлов для каждого расширения различно.
#✔ Внутри используйте вызов функции из прошлой задачи.
from sys import path
#For absolute import, support if __name__ == "__main__"
path.append('../')
#Absolute package import
from module import shfutil
from sys import argv

if len(argv) > 1:    
    if shfutil.generatorext(**{value.split('=')[0]:int(value.split('=')[1]) for value in argv[1:]}):
        print("Sucess complited!")
    else:
        print("Error operation!")
else:
    print(help(shfutil.generatorext))