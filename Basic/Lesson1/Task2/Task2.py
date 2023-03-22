#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('Input X:'))
y = int(input('Input Y:'))
z = int(input('Input Z:'))

print((~(x | y | z) == ~x & ~y & ~z))