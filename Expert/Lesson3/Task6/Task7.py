#✔ Пользователь вводит строку текста.
#✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
#✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
#✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
from typing import Dict

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

def str_count(text: str) -> Dict[str, int]:
    result = dict()
    for item in set(text):
        result[item] = text.count(item)
    return result

def for_count(text: str) -> Dict[str, int]:
    result = dict()
    for item in set(text):
        result[item] = 0
        for char in text:
            if char == item:
                result[item] = result[item] + 1
    return result

text = try_castinput("Input text:", str)
#ключи совпадают поскольку при формирования 
#словоря в обоих вариантах использовалось множество
print(f"result str_count:{str_count(text)}")
print(f"result for_count:{for_count(text)}")