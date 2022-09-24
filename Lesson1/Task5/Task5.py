#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
from math import sqrt

class Point:
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)
	def distance(self, point):
		return round(sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2), 2);

point = list(map(int, input('Input point A(X,Y):').split(',')))
a = Point(point[0], point[1])
point = list(map(int, input('Input point B(X,Y):').split(',')))
b = Point(point[0], point[1])

print(f'Distance={b.distance(a)}')