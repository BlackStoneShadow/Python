#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
from math import pow

def is_int(number):
    return number.isdigit()

def function(number):
    if number in (1, 2): 
        return 1
    
    return function(number - 1) + function(number - 2)

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

result = list()
for i in range(-number, number + 1):
    if i != 0: 
        result.append(int(pow(i / abs(i), i + 1) * function(abs(i))))
    else:
        result.append(0)

print(result)