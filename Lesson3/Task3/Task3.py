#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import randint

def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

result = list(map(lambda i: round(i / randint(i, number), 2), range(1, number + 1)))

min_rest = 1
max_rest = 0
for i in result:
    if i % 1 < min_rest: min_rest = i % 1
    if i % 1 > max_rest: max_rest = i % 1

print(result, '->', max_rest - min_rest)