#Задайте натуральное число N. 
#Напишите программу, которая составит список простых множителей числа N.
from math import sqrt

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

def is_simple(number, numbers):
    for i in numbers:
        if i > sqrt(number):
            return True
        elif not number % i:
            return False
    return True

number = try_castinput("Input number:", int)

simple_numbers = list()

for num in range(2, number):
    if is_simple(num, simple_numbers): 
        simple_numbers.append(num)

result = [(num, number // num) for num in simple_numbers if not number % num]

print(result)