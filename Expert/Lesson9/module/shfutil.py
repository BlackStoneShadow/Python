import csv
import json
from functools import wraps
from pathlib import Path
from random import randint
from typing import Tuple
from typing import Callable

_MIN = 100
_MAX = 1000

__all__ = ['run']

def save_csv(name: str, count: int = 1):
    def deco(func: Callable):
        def wrapper(num: int):
            try:
                names=("a", "b", "c")
                with open(Path(name) / "member.csv", "w", newline="", encoding="utf-8") as f:        
                    csv_writer = csv.DictWriter(f, fieldnames=list(names), dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)   
                    csv_writer.writeheader()
                    for _ in range(count):
                        csv_writer.writerow(dict(zip(names, func(num))))     
                
                return True
            except:
                return False
        
        return wrapper
    return deco
            
def save_json(name: str):
    def deco(func: Callable):
        def wrapper(a: int = 0, b: int = 0, c: int = 0):
            try:
                result = list()
                with open(Path(name) / "member.csv", "r", encoding="utf-8") as f:        
                    csv_reader = csv.DictReader(f, ["a", "b", "c"], dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)
                    for num, row in enumerate(csv_reader):
                        if num > 0:
                            row["result"] = func(row['a'], row['b'], row['c'])
                            result.append(row)
                
                with open(Path(name) / "result.json", "w", encoding="utf-8") as f:        
                    json.dump(result, f)

                return True
            except:
                return False
        
        return wrapper
    return deco
    

@save_csv(Path().cwd() / "..\module\Data", randint(_MIN, _MAX))                    
def member(num: int)->Tuple[int, int, int]:
    """
    функция генерации коэффициетов.

    параметры:
    num     - максимальное значение коэффициента
    """

    return (randint(1, num), randint(1, num), randint(1, num))

@save_json(Path().cwd() / "..\module\Data")
def root(a: int = 0, b: int = 0, c: int = 0)->Tuple[float, float]:
    """
    функция поиска корней.

    параметры:
    a, b, c - значение коэффициентов
    """
    try:
        D = b**2 - 4 * a * c

        if D == 0:
            return (-b + D**0.5 / (2 * a), -b - D**0.5 / (2 * a))
        elif D > 0:
            return (-b / (2 * a), 0)
        else: 
            raise ValueError
    except:
        return None

def run(num: int)->bool:
    """
    функция поиска корпней квадратных уравнений.

    параметры:
    num     - максимальное значение коэффициента
    """
    try:
        if member(num):
            return root()
        else:
            raise ValueError
    except:
        return False

if __name__ == "__main__": 
    run(100)