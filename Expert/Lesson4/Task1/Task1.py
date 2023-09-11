#Напишите функцию для транспонирования матрицы
from typing import Tuple

def transporent(matrix:Tuple[Tuple[str]])->Tuple[Tuple[str]]:
  return tuple(zip(*matrix[::-1]))

print(transporent
 (
    [
        ['a','b','c'],
        ['d', 'e', 'f'],
        ['g', 'i', 'j']]
    )
 )