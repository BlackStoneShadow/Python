#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
from math import sqrt

class Point:
	def __init__(self, X, Y):
		self.X = int(X)
		self.Y = int(Y)
	def Distance(Self, Point):
		return round(sqrt((Point.X - Self.X) ** 2 + (Point.Y - Self.Y) ** 2), 2);

point = list(map(int, input('Input point A(X,Y):').split(',')))
A = Point(point[0], point[1])
point = list(map(int, input('Input point B(X,Y):').split(',')))
B = Point(point[0], point[1])

print(f'Distance={B.Distance(A)}')