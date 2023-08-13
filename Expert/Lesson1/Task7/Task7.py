#Пользователь вводит число от 1 до 999. Используя операции с числами
#сообщите что введено: цифра, двузначное число или трёхзначное число.
#Для цифры верните её квадрат, например 5 - 25
#Для двузначного числа произведение цифр, например 30 - 0
#Для трёхзначного числа его зеркальное отображение, например 520 - 25
#Если число не из диапазона, запросите новое число
#Откажитесь от магических чисел
#В коде должны быть один input и один print
def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

MIN = 1
MAX = 1000

num = None
while num == None:
    num = try_castinput(f"Inupt number from {MIN} to {MAX-1}:", int)
    if not(num in range(MIN, MAX)): num = None

if int(num / 10) == 0:
    message = f"{num} is number, square={num**2}"
elif int(num / 100) != 0:
    message = f"{num} is three digit number, mirror={int(str(num)[::-1])}"
else:
    message = f"{num} is two digit number, product={int(num/10)*int(num%10)}"

print(message)