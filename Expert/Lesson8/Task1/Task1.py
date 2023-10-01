#Напишите функцию, которая получает на вход директорию и рекурсивно
#обходит её и все вложенные директории. Результаты обхода сохраните в
#файлы json, csv и pickle.
#Для дочерних объектов указывайте родительскую директорию.
#Для каждого объекта укажите файл это или директория.
#Для файлов сохраните его размер в байтах, а для директорий размер
#файлов в ней с учётом всех вложенных файлов и директорий.
from sys import path
#For absolute import, support if __name__ == "__main__"
path.append('../')
#Absolute package import
from module import shfutil
from pathlib import Path
from sys import argv

if len(argv) == 3 and argv[1] == "ls":
    shfutil.print_tree(Path(Path().cwd() / argv[2]))
elif len(argv) == 2 and argv[1] == "ls":
    print(help(shfutil.print_tree))
elif len(argv) == 3 and argv[1] == "csv":
    if shfutil.save_csv(Path(Path().cwd() / argv[2])):
        print("save in list.csv")
    else:
        print("error")
elif len(argv) == 2 and argv[1] == "csv":
    print(help(shfutil.save_csv))
elif len(argv) == 3 and argv[1] == "json":
    if shfutil.save_json(Path(Path().cwd() / argv[2])):
        print("save in list.json")
    else:
        print("error")
elif len(argv) == 2 and argv[1] == "json":
    print(help(shfutil.save_json))
elif len(argv) == 3 and argv[1] == "bin":
    if shfutil.save_bin(Path(Path().cwd() / argv[2])):
        print("save in list.pickle")
    else:
        print("error")
elif len(argv) == 2 and argv[1] == "bin":
    print(help(shfutil.save_bin))
else:    
    print('Task1.py "ls|csv|json|bin" "Dir"')