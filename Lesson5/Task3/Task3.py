#Создайте программу для игры в ""Крестики-нолики"".
from random import randint
from os import system
from View import print_matrix

SIZE = 3

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

def input_palyer():
    return [try_castinput('Input row:', int), try_castinput('Input col:', int)]

def input_palyer1(name):
    if name:
        return "player1"
    else:
        return input_palyer()

def input_palyer2(name):
    if name:
        return "player2"
    else:
        return input_palyer()

def input_bot(name):    
    if name:
        return "bot"
    else:
        return [randint(1, SIZE), randint(1, SIZE)]

def input_step(play):    
    result = [0, 0]
    print(play(True))   
    while not (0 < result[0] <= SIZE and 0 < result[1] <= SIZE):
        result = play(False)               
    return result

#def print_matrix(matrix):
#    system('cls')
#    print('\n'.join([str().join(['{:4}'.format(item) for item in row]) for row in matrix]))

def finish(matrix):
    symbol = str()
    #Строки
    for i in range(SIZE):
        if symbol != str(): 
            break
        symbol = matrix[i][0]
        for j in range(1, SIZE):
            if matrix[i][j] != symbol:
                symbol = str()
                break

    if symbol != str():
        return symbol
    #Колонки
    for i in range(SIZE):
        if symbol != str(): 
            break
        symbol = matrix[0][i]
        for j in range(1, SIZE):
            if matrix[j][i] != symbol:
                symbol = str()
                break

    if symbol != str():
        return symbol
    #Прямая диагональ
    symbol = matrix[0][0]    
    for i in range(1, SIZE):
        if matrix[i][i] != symbol:
            symbol = str()
            break
    
    if symbol != str():
        return symbol
    #Обратная диагональ
    symbol = matrix[0][SIZE - 1]    
    for i in range(1, SIZE - 1):
        if matrix[i][SIZE - (i + 1)] != symbol:
            symbol = str()
            break
    
    if symbol != str():
        return symbol
    #Ничья
    symbol = '*'
    for i in range(SIZE):
        for j in range(1, SIZE):
            if matrix[i][j] == str():
                symbol = str()
                break

    return symbol

def play(player1, player2):
    if randint(1, 2) % 2 == 0:
        player1, player2 = player2, player1    
    
    matrix = [[str() for col in range(SIZE)] for row in range(SIZE)]
    
    motion = 0
    while True:                
        if motion % 2 == 0:
            player = player1
        else: 
            player = player2
        
        if player == player1:
            symbol = 'O'
        else:
            symbol = 'X'

        while True:
            step = input_step(player)
            symbol_old, matrix[step[0] - 1][step[1] - 1] = matrix[step[0] - 1][step[1] - 1], symbol            
            if symbol_old == str():
                break
            else:
                matrix[step[0] - 1][step[1] - 1] = symbol_old
        
        print_matrix(matrix)
        
        symbol = finish(matrix)

        if symbol == 'O':
            print('Winner:', player1(True))        
            break
        elif symbol == 'X':
            print('Winner:', player2(True))        
            break
        elif symbol == '*':
            print('Drawn:')        
            break
        else:
            motion += 1

player_2 = None
while player_2 not in ('p', 'b'):
    system('cls')
    player_2 = try_castinput('input second player(player=p, bot=b):', str)

if  player_2 == 'p':
    play(input_palyer1, input_palyer2)    
else:
    play(input_palyer1, input_bot)    