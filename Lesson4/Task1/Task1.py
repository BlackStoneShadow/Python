#Вычислить число c заданной точностью d
#Пример:- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from math import pi

def get_digit(text):
    result = text
    if result[0] == '-':
        result = result[1:]
    
    return result.replace('.', '', 1)

def is_float(number):   
    return get_digit(number).isdigit()

number = None

while not is_float(str(number)):
    number = input("Input number:")

number = float(number)

print('pi->', round(int(pi / number) * number, 10)) 