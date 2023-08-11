#3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

num = None
while num == None: 
    num = try_castinput("Input number:", int)
    if 100000 < num or num < 0 : num = None

message = "число простое"
for i in range(2, num - 1):
    if num % i == 0:
        message = "число составное"

input(message)