from pathlib import Path
from typing import TypeVar
from typing import List

__all__ = ['dir_tree']
 
def dir_tree(name: str)->List[TypeVar(str, str, str, float)]:
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
                childs = dir_tree(Path(item.parent / item.name))
                if len(childs) > 0:
                    result = sorted(result + childs)
                    size = sum(map(lambda item: float(item[3]), childs))
            result.append((str(item.parent), item.name, 'Dir' if item.is_dir() else 'File' if item.is_file() else 'Link', size))
        
        result.sort(key=lambda item: (item[2], item[0]))        

        return result
    except:
        return result
 
if __name__ == "__main__": 
    print(dir_tree(Path().cwd() / "Data"))
