#Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
#должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
#числа используйте код:
#from random import randint
#num = randint(LOWER_LIMIT, UPPER_LIMIT) 
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
STEP_LIMIT  = 10

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

num = randint(LOWER_LIMIT, UPPER_LIMIT) 

message = "Incorrectly!"
for i in range(STEP_LIMIT):
    answer = try_castinput(f"input number from {LOWER_LIMIT} to {UPPER_LIMIT}:", int)
    if answer < num:
        print("less")       
    elif answer > num:
        print("over")
    else:
        message = "Winner!"
        break        

print(message)