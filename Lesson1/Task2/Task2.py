#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
X = int(input('Input X:'))
Y = int(input('Input Y:'))
Z = int(input('Input Z:'))

if(~(X | Y | Z) == ~X & ~Y & ~Z):
	print('Yes')
else:
	print('No')
