#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)) or int(number) % 2 != 0:
    number = input("Input number:")

number = int(number)

array = list(range(number))

result = list()

for i in range(0, int(number / 2)):
    result.append(array[i] * array[number - (i + 1)])

print(array, '->', result)