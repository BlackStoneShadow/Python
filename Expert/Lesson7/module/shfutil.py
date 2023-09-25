from os import urandom
from pathlib import Path
from typing import Tuple
from random import uniform
from random import choice
from random import randint
from string import ascii_lowercase 

__all__ = ['fun_gen', 'func_name', 'func_sum', 'rename', 'generator', 'generatorext']
 
_MIN_NUMBER = -1000
_MAX_NUMBER = 1000

def fun_gen(num_str: int, file_name: str):
    """
    функцию заполняющая файл 
    (добавляет в конец) случайными парами чисел. 
    Первое число int, второе - float разделены вертикальной чертой. 
    Минимальное число - -1000, максимальное - +1000. 
    Количество строк и имя файла передаются как аргументы функции. 
    """
    with open(Path().cwd() / "Data" / file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            int_num = randint(_MIN_NUMBER, _MAX_NUMBER)
            float_num = uniform(_MIN_NUMBER, _MAX_NUMBER)
            f.write(f'{int_num}|{float_num:.2f}\n')

def func_name(num, new_file):
    """
    функцию генерирующая псевдоимена. 
    Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
    среди которых обязательно должны быть гласные. 
    Полученные имена сохраните в файл.
    """
    with open(Path().cwd() / "Data" / new_file, 'a', encoding='utf-8') as f:
        for _ in range(num):
            res = ''
            for _ in range(randint(4,7)):
                a = chr(randint(1072, 1104))
                res += a
            glas = 'аяуюоеёэиы'
            res += choice(glas)
            f.write(f'{res.title()}\n')

def func_sum(file1, file2):
    """
    функция открывающая на чтение созданные в прошлых задачах файлы с числами и именами.
    Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
    В результирующем файле должно быть столько же строк, сколько в более длинном файле. 
    При достижении конца более короткого файла, возвращайтесь в его начало.
    """
    with open(Path().cwd() / "Data" / file1, 'r', encoding='utf-8') as f1:
        with open(Path().cwd() / "Data" / file2, 'r', encoding='utf-8') as f2:
            with open(Path().cwd() / "Data" / 'res.txt','w', encoding='utf-8') as res:
                digit = f1.readlines()
                name = f2.readlines()
                max_len = max(len(digit), len(name))
                min_len = min(len(digit), len(name))
                rate = max_len// min_len
                rate2 = max_len % min_len 
                if len(digit) > len(name):
                    name *= rate
                    name += name[:rate2]
                else:
                    digit *= rate
                    digit += digit[:rate2]
                for i in range(max_len):
                    a = eval(digit[i].replace('|', '*'))
                    b = name[i].replace('\n', '')
                    res.write(f'{b} = {a}\n')
            
def rename(name: str, digit: str, sext: str, dext: str, rang: Tuple[int, int])->bool:   
    """
    групповое переименование файлов
    
    параметры:
    name    - желаемое конечное имя файлов
    digit   - количество цифр в порядковом номере
    sext    - расширение исходного файла
    dext    - расширение конечного файла
    rang    - диапазон сохраняемого оригинального имени
    пример вызова:
    Task2.py "_new_" "{:03}" ".txt" ".bak" 0 4
    """  
    try:
        sext = '.' + sext
        dext = '.' + dext
        for count, item in enumerate(filter(lambda i: i.is_file() and i.suffix == sext, Path(Path().cwd() / "Data").iterdir())):            
            Path(item).rename(Path(item.parent / f"{item.stem[rang[0]:rang[1]]}{name}{digit.format(count)}").with_suffix(dext))

        return True
    except:
        return False
 
def generator(ext: str, min_len: int = 6, max_len: int = 30, min_data: int = 256, max_data: int = 4096, count: int = 42)->bool:   
    """
    создание файлы с указанным расширением
    
    параметры:
    ext         - расширение файлов
    min_len     - минимальная длина случайно сгенерированного имени
    max_len     - максимальная длина случайно сгенерированного имени
    min_data    - минимальное число случайных байт
    max_data    - максимальное число случайных байт
    count       - количество файлов
    пример вызова:
    Task1.py "txt" 6 30 256 4096 1
    """  
    try:
        ext = '.' + ext        
        for i in range(count):
            name: str = str()
            for _ in range(randint(min_len, max_len)):
                name += choice(ascii_lowercase)                                         
            Path(Path(Path().cwd() / "Data")).mkdir(parents=True, exist_ok=True)
            with open(Path(Path().cwd() / "Data" / name).with_suffix(ext), 'bw') as f:
                f.write(urandom(randint(min_data, max_data)))

        return True
    except:
        return False

def generatorext(**kwargs):
    """
    генерирует файлы с разными расширениями
    параметры:
    расширения = количество
    пример:
    txt = 1, pdf = 2
    """   
    for key, items in kwargs.items():
        if not generator(ext = key, count = items):
            return False
    return True

if __name__ == "__main__": 
    fun_gen(5, 'new_file.txt')
    func_name(5, 'new_file1.txt')
    func_sum('new_file.txt', 'new_file1.txt')
    rename("_new_", '{:03}', "txt", "bak", (0,4))
    generator("txt", 6, 30, 256, 4096, 1)
    generatorext(txt = 1, pdf = 2)