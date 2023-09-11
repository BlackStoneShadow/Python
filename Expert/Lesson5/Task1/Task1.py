#Напишите функцию, которая принимает на вход строку —
#абсолютный путь до файла. Функция возвращает кортеж из трёх
#элементов: путь, имя файла, расширение файла.from typing import Tuple

def path_elements(path:str)->Tuple[str]:
  return (str('\\').join(path.split('\\')[:-1]), path.split('\\')[-1].split('.')[0], path.split('\\')[-1].split('.')[1])

print(path_elements(input("input the full file name:")))