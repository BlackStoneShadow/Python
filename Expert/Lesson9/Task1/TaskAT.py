import csv
import json
from functools import wraps
from random import randint
from typing import Callable
from sys import argv

_MIN_ = 100
_MAX_ = 1000

def save_to_json(func: Callable):    
    @wraps(func)
    def wrapper(*args):
        try:            
            results = list()
            with open(args[0], "r", encoding="utf-8") as f:        
                csv_reader = csv.DictReader(f, ["a", "b", "c"], dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)
                for num, row in enumerate(csv_reader):
                    if num > 0:
                        row["result"] = func(row['a'], row['b'], row['c'])
                        results.append(row)
                
            with open("results.json", "w", encoding="utf-8") as f:        
                json.dump(results, f)

            return True
        except:
            return False
        
    return wrapper

def generate_csv_file(file_name: str, rows: int):
    try:
        names = ("a", "b", "c")
        with open(file_name, "w", newline="", encoding="utf-8") as f:        
            csv_writer = csv.DictWriter(f, fieldnames=list(names), dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)   
            csv_writer.writeheader()
            for _ in range(rows):
                csv_writer.writerow(dict(zip(names, (randint(1, 100) for _ in range(3)))))     
        return True
    except:
        return False

@save_to_json            
def find_roots(a, b, c):
    """
    функция поиска корней.

    параметры:
    a, b, c - значение коэффициентов
    """
    try:
        D = b**2 - 4 * a * c

        if D == 0:
            return -b / (2 * a)
        elif D > 0:
            return -b + D**0.5 / (2 * a), -b - D**0.5 / (2 * a)            
        else: 
            raise ValueError
    except:
        return None

count = randint(_MIN_, _MAX_)
    
generate_csv_file("input_data.csv", count)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if _MIN_<=len(data)<=_MAX_:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==count)    
