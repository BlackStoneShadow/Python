#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def is_int(number):
    return number.isdigit()

number = None

while not is_int(str(number)):
    number = input("Input number:")

number = int(number)

result = []
for i in range(1, number+1):
    result.append(round((1 + 1 / i) ** i))

sum = 0
for i in result: 
    sum += i

print(result, '->', sum)
