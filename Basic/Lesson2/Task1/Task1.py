#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

def get_digit(text):
    result = text
    if result[0] == '-':
        result = result[1:]    
    #заменить только первое вхождение,
    #при дальнейших вхождениях isdigit = false
    result = result.replace('.', '', 1) 

def is_digit(number):   
    return get_digit(number).isdigit()

number = None

while not is_digit(str(number)):
    number = input("Input number:")

sum = 0
for i in get_digit(number):
    sum += int(i)

print(number, '->', sum)
