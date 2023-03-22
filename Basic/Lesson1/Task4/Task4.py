#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y).
n = 0

while n < 1 or n > 4:
	n = int(input('Input N:'))

if n == 1:
	print('X > 0 and Y > 0')
elif n == 2:
	print('X < 0 and Y > 0')
elif n == 3:
	print('X < 0 and Y < 0')
elif n == 4:
	print('X > 0 and Y < 0')
