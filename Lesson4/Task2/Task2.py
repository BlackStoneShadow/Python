#Задайте натуральное число N. 
#Напишите программу, которая составит список простых множителей числа N.
from math import sqrt

def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

result = [(num, int(number / num)) for num in range(1, number + 1) if not number % num]

print(result)