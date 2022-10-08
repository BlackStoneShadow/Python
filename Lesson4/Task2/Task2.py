#Задайте натуральное число N. 
#Напишите программу, которая составит список простых множителей числа N.

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

number = try_castinput("Input number:", int)

result = [(num, number // num) for num in range(1, number + 1) if num % 2 and num % 3 and not number % num]

print(result)