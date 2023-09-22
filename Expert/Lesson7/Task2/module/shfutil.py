from pathlib import Path
from typing import Tuple

__all__ = ['rename']
 
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
        for count, item in enumerate(filter(lambda i: i.is_file() and i.suffix == sext, Path(Path().cwd() / "Data").iterdir())):            
            Path(item).rename(Path(item.parent / f"{item.stem[rang[0]:rang[1]]}{name}{digit.format(count)}").with_suffix(dext))

        return True
    except ValueError:
        return False

if __name__ == "__main__":    
    rename("_new_", '{:03}', ".txt", ".bak", (0,4))