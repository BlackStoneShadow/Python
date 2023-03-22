#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input("Input number:")

result = [1]
for i in range(1, int(number)):
    result.append(result[i - 1] * (i + 1))

print(result)