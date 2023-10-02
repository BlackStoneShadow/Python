#Напишите функцию, которая ищет json файлы в указанной
#директории и сохраняет их содержимое в виде
#одноимённых pickle файлов.
from sys import path
#For absolute import, support if __name__ == "__main__"
path.append('../')
#Absolute package import
from module import shfutil
from pathlib import Path
from sys import argv

if len(argv) == 2:
    if shfutil.convert_jsontobin(Path(Path().cwd() / argv[1])):
        print("convert sucess")
    else:
        print("convert error")
else:
    print(help(shfutil.convert_jsontobin))