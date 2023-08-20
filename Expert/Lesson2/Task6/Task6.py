#Задание №6
#Напишите программу банкомат.
#✔ Начальная сумма равна нулю
#✔ Допустимые действия: пополнить, снять, выйти
#✔ Сумма пополнения и снятия кратны 50 у.е.
#✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
#✔ Нельзя снять больше, чем на счёте
#✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
#операцией, даже ошибочной
#✔ Любое действие выводит сумму денегfrom os import systemMULT = 50
OPRC = 0.015
IPRC = 0.03
TPRC = 0.1
OMIN = 30
OMAX = 600
SMAX = 5_000_000

count: int = 0
balance: float = 0 

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

def Add(value: int) -> bool:
    global count    
    global balance

    balance -= balance * TPRC if balance > SMAX else 0

    if value % MULT == 0:
        count += 1

        balance += value
        
        balance += balance * IPRC if count % 3 == 0 else 0

        return True
    else:
        return False

def Remove(value: int) -> bool:        
    global count
    global balance

    balance -= balance * TPRC if balance > SMAX else 0           
    
    value += (0 if value % MULT == 0 else balance) + (OMIN if value * OPRC < OMIN else OMAX if OMAX < value * OPRC else value * OPRC)
    
    if balance - value >= 0:
        count += 1

        balance -= value
        balance += balance * IPRC if count % 3 == 0 else 0

        return True
    else:
        return False

while True:
    system("cls")

    print("I_nput")
    print("O_nput")
    print("E_xit")

    print(f"Balance={balance}")

    Symbol = try_castinput("Input command:", str)

    if Symbol == "I":
        while not Add(try_castinput("Input the deposit amount:", int)):
            print("Error input!")
    elif Symbol == "O":
        while not Remove(try_castinput("Input the debit amount:", int)):
            print("Error input!")        
    elif Symbol == "E":
        break
    else:
        print("Incorrect input!")    
