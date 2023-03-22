#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
enum_number = list(map(int, input("input list:").split()))

enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))

print(enum_number, '->', enum_unique)