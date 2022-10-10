#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. 
#Играют два игрока делая ход друг после друга. 
#Первый ход определяется жеребьёвкой. 
#За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""
from os import system
from random import randint

MAX_COUNT = 2021
MAX_STEP = 28

def try_castinput(message, type):
    result = str()
   
    try:
        result = type(input(message))
    except:
        result = try_castinput(message, type)

    return result

def input_palyer(message):
    return try_castinput(message, int)
def input_palyer1(name, count = 0):
    if name:
        return "player1"
    else:
        return input_palyer('Input player1 count:')
def input_palyer2(name, count = 0):
    if name:
        return "player2"
    else:
        return input_palyer('Input player2 count:')
def input_bot(name, count = 0):    
    if name:
        return "bot"
    else:
        result = randint(1, MAX_STEP)
        print('Input bot count:', result)
        return result
def input_smartbot(name, count = 0):    
    if name:
        return "smartbot"
    else:
        result = MAX_COUNT % (MAX_STEP + 1)

        if count != 0: 
            result = (MAX_STEP + 1) - count

        print('Input bot count:', result)

        return result
def input_count(play, count):
    result = 0
    while not 0 < result < MAX_STEP + 1:
        result = play(False, count)               
    return result

def play(player1, player2):
    if randint(1, 2) % 2 == 0 or player2(True) == 'smartbot':
        player1, player2 = player2, player1
    
    play_sum, prev_sum, idx = 0, 0, 0
    while play_sum != MAX_COUNT:          
        print('rest:', MAX_COUNT - play_sum)            
        
        if idx % 2 == 0:
            player = player1
        else: 
            player = player2
        
        count = MAX_COUNT + 1
        while MAX_COUNT - (play_sum + count) < 0:
            count = input_count(player, play_sum - prev_sum)
        
        if player(True) not in ('bot', 'smartbot'):
            system('cls')

        prev_sum = play_sum
        play_sum += count
        idx += 1               

    print('Winner:', player(True))        

player_2 = None
while player_2 not in (1, 2, 3):
    system('cls')
    player_2 = try_castinput('input second player(player=1, bot=2 or smartbot=3):', int)

if  player_2 == 1:
    play(input_palyer1, input_palyer2)    
elif player_2 == 2:
    play(input_palyer1, input_bot)    
else:
    play(input_palyer1, input_smartbot)    