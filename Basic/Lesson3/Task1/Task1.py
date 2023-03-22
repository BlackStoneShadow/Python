#Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

array = list(range(number))

sum_even = 0

for i in array:
    if i % 2 != 0: sum_even += array[i]

print(array, '->', sum_even)