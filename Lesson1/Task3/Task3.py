#Напишите программу, которая принимает на вход координаты точки (X и Y), 
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

X = 0
Y = 0

while X == 0 and Y == 0:
	X = int(input('Input X:'))
	Y = int(input('Input Y:'))

	if X > 0 and Y > 0:
		print(1)
		break
	elif X < 0 and Y > 0:
		print(2)
		break
	elif X < 0 and Y < 0:
		print(3)
		break
	elif X > 0 and Y < 0:
		print(4)
		break
	else:
		print('Error input!')