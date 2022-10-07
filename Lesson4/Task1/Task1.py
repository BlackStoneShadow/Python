#Вычислить число c заданной точностью d
#Пример:- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from math import pi

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

number = try_castinput("Input number:", float)

print('pi->', round(int(pi / number) * number, 10)) 