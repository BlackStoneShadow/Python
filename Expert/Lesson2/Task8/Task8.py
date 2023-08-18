#Напишите программу, которая принимает две строки
#вида “a/b” — дробь с числителем и знаменателем.
#Программа должна возвращать сумму
#и *произведение дробей. Для проверки своего
#кода используйте модуль fractions.
from typing import Tuple
from fractions import Fraction
from fractions import gcd

def parse(frct:str)->Tuple[int,int]:
    return frct.split("/")

def sum_frac(f1:str, f2:str)->str:
    a1,b1 = map(int, parse(f1))
    a2,b2 = map(int, parse(f2))
   
    num = a1 * b2 + a2 * b1
    den = b1 * b2
    dev = gcd(num, den)

    return f"{int(num/dev)}/{int(den/dev)}" if num != den else str(int(num/dev))

def mlt_frac(f1:str, f2:str)->str:
    a1,b1 = map(int, parse(f1))
    a2,b2 = map(int, parse(f2))
   
    num = a1 * a2
    den = b1 * b2
    dev = gcd(num, den)

    return f"{int(num/dev)}/{int(den/dev)}" if num != den else str(int(num/dev))

f1: str =  input("Input fraction1:")
f2: str =  input("Input fraction2:")

print(f"{f1} + {f2} = {sum_frac(f1, f2)} <=> {Fraction(f1) + Fraction(f2)}")
print(f"{f1} * {f2} = {mlt_frac(f1, f2)} <=> {Fraction(f1) * Fraction(f2)}")