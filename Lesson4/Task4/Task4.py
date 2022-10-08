#Задана натуральная степень k. 
#Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

def get_operand(num, pwr):
    if pwr == 0:
        return str(num)
    elif pwr == 1:
        return str(num) + "x"
    else:
        return str(num) + "x^" + str(pwr)

k = try_castinput("Input extent:", int)

operands = list()

for i in range(k, -1, -1):
    operands.append(get_operand(randint(0, 100), i))

result = " + ".join(operands) + ' = 0'

with open('File.txt', 'w') as data:
    data.write(result)