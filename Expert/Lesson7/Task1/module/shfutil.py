from os import urandom
from pathlib import Path
from random import choice
from random import randint
from string import ascii_lowercase 

__all__ = ['generator']
 
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
    Task1.py ".txt" 6 30 256 4096 1
    """  
    try:
        for i in range(count):
            name: str = str()
            for _ in range(randint(min_len, max_len)):
                name += choice(ascii_lowercase)            
            with open(Path(Path().cwd() / "Data" / name).with_suffix(ext), 'bw') as f:
                f.write(urandom(randint(min_data, max_data)))

        return True
    except ValueError:
        return False

if __name__ == "__main__":    
    generator(".txt", 6, 30, 256, 4096, 1)