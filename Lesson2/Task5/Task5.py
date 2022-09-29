#Реализуйте алгоритм перемешивания списка.
from random import randint

def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

result = []
for i in range(number):
    result.append(i)

print(result)

for i in result:
    index = randint(0, number - 1)
    
    temp = result[0]    
    result[0] = result[index]   
    result[index] = temp  

print(result)