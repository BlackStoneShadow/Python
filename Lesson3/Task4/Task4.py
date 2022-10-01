#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10
def is_int(number):
    return number.isdigit()

def convert(number):
    result = ''
    
    term = int(number / 2)
    
    if term > 0:         
        result = convert(term) + str(number - term * 2)
    else:
        result = str(number)

    return result

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

print(number, '->', convert(number))