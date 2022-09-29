#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

def is_int(number):
    return number.replace('\n', '').isdigit()

def read_oper(data):
    text = data.readline()
    
    if is_int(text):
        return int(text)
    else:
        return None

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

lists = []
for i in range(number):
    lists.append(randint(-number, number))

print(lists)

result = []
with open('file.txt', 'r') as data:
    while True:
        oper1 = read_oper(data)
        if oper1 == None: break
        
        oper2 = read_oper(data)
        if oper1 == None: break

        if 0 <= oper1 < number and 0 <= oper2 < number:
            result.append(lists[oper1] * lists[oper2])
        
print(result)