#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).
N = 0

while ~(0 < N < 5):
	N = int(input('Input N:'))

	if N == 1:
		print('X > 0 and Y > 0')
		break
	elif N == 2:
		print('X < 0 and Y > 0')
		break
	elif N == 3:
		print('X < 0 and Y < 0')
		break
	elif N == 4:
		print('X > 0 and Y < 0')
		break
	else:
		print('Error input!')