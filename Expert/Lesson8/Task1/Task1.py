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

if len(argv) == 2:
    print(f"{'Type':<5}{'Size':<5}{'Name'}")
    for item in shfutil.dir_tree(Path(Path().cwd() / argv[1])):
        print(f"{item[2]:<5}{item[3]:<5}{Path(Path(item[0])/Path(item[1]))}")
else:
    print(help(shfutil.dir_tree))