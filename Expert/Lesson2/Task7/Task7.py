#Напишите программу, которая получает целое
#число и возвращает его шестнадцатеричное
#строковое представление. Функцию hex
#используйте для проверки своего результата.
BASE = 16

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

num = try_castinput(f"Inupt number:", int)

print(f'hex={hex(num)}')

result: str = str()
while num > 0:
    result = ('A' if num % BASE == 10 else 'B' if num % BASE == 11 else 'C' if num % BASE == 12 else 'D' if num % BASE == 13 else 'E' if num % BASE == 14 else 'F' if num % BASE == 15 else str(num % BASE)) + result
    num = num // BASE    

print(f'Hex={result}')