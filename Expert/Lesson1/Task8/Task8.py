#Нарисовать в консоли ёлку спросив у пользователя количество рядов.
def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

n = try_castinput("Enter rows count:", int)

for i in range(1, n + 1):
    for j in range(1, n*2 + 1):
        if n - i < j < n + i :
            print("*", end="" if j < n*2 else "\n")
        else:
            print(" ", end="" if j < n*2 else "\n")