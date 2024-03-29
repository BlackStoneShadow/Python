import csv
import json
import pickle
from pathlib import Path
from typing import TypeVar
from typing import List

__all__ = ['print_tree', 'save_csv', 'save_json', 'save_bin']
 
def tree(name: str)->List[TypeVar(str, str, str, float)]:
    """
    функция рекурсивного обхода директорий.
    
    параметры:
    name    - корневая директория

    пример вызова:
    Task1.py "Data"
    """  
    try:
        result = list()
        for item in Path(name).iterdir():            
            size: float = item.stat().st_size
            if item.is_dir():
                childs = tree(Path(item.parent / item.name))
                if len(childs) > 0:
                    result = sorted(result + childs)
                    size = sum(map(lambda item: int(item[3]) if item[2] == "File" else 0, childs))
            result.append((str(item.parent), item.name, "Dir" if item.is_dir() else "File" if item.is_file() else "Link", size))
        
        result.sort(key=lambda item: (item[2], item[0]))        

        return result
    except:
        return result

def print_tree(name: str)->bool:
    """
    функция вывода на консоль структуры каталога

    параметры:
    name    - корневая директория

    пример вызова:
    Task1.py "ls" "Data"
    """
    try:
        print(f"{'Type':<5}{'Size':<5}{'Name'}")
        for item in tree(name):
            print(f"{item[2]:<5}{item[3]:<5}{Path(Path(item[0])/Path(item[1]))}")

        return True
    except:
        return False


def save_csv(name: str)->bool:
    """
    функция сохранения в файл csv структуры каталога

    параметры:
    name    - корневая директория

    пример вызова:
    Task1.py "csv" "Data"
    """
    try:
        with open(Path(name) / "list.csv", "w", newline="", encoding="utf-8") as f:
            names=("dir", "name", "type", "size")
            csv_writer = csv.DictWriter(f, fieldnames=list(names), dialect="excel-tab", quoting=csv.QUOTE_NONNUMERIC)        
            csv_writer.writeheader()
            for item in tree(name):
                csv_writer.writerow(dict(zip(names, (item[0], item[1], item[2], item[3]))))
        
        return True
    except:
        return False

def save_json(name: str)->bool:
    """
    функция сохранения в файл json структуры каталога

    параметры:
    name    - корневая директория

    пример вызова:
    Task1.py "json" "Data"
    """
    try:
        with open(Path(name) / "list.json", "w", encoding="utf-8") as f:
            json.dump({str(Path(Path(item[0]) / Path(item[1]))) : (item[0], item[1], item[2], item[3]) for item in tree(name)}, f, ensure_ascii=False)

        return True
    except:
        return False

def save_bin(name: str)->bool:
    """
    функция сохранения в двоичный файл структуры каталога

    параметры:
    name    - корневая директория

    пример вызова:
    Task1.py "bin" "Data"
    """
    try:
        with open(Path(name) / "list.pickle", "wb") as f: 
            pickle.dump({str(Path(Path(item[0]) / Path(item[1]))) : (item[0], item[1], item[2], item[3]) for item in tree(name)}, f)
        
        return True
    except:
        return False

def convert_jsontobin(name: str)->bool:
    """
    функция преобразования файлов json в двоичный формат

    параметры:
    name    - корневая директория

    пример вызова:
    Task5.py "Data"
    """
    try:
        sext: str = '.' + 'json'
        dext: str = '.' + 'pickle'
        for item in filter(lambda i: i.is_file() and i.suffix == sext, Path(name).iterdir()):                        
            with open(str(item), 'r') as f:
                data = json.loads(f.read())
                with open(Path(item.parent / item.name).with_suffix(dext), "wb") as f:
                    pickle.dump(data, f)

        return True
    except:
        return False

if __name__ == "__main__": 
    print_tree(Path().cwd() / "Data")
    save_csv(Path().cwd() / "Data")
    save_json(Path().cwd() / "Data")
    save_bin(Path().cwd() / "Data")
    convert_jsontobin(Path().cwd() / "Data")
