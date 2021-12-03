import math
from scipy import integrate
from numpy import *


def f1(x):
    return 1 / sqrt(x + 4)


def left(f1, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(0, n):
        sum += f1(a + i * h)
    return sum * h

def right(f1, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(1, n + 1):
        sum += f1(a + i * h)
    return sum * h

def aver(f1, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(0, n):
        sum += f1(a + i * h)
    return sum * h
  
c1, err = integrate.quad(f1, 0.5, 2.3)   
print("Method of rectangle")
print("left rectangle:", left(f1, 0.5, 2.3, 10))
print("right rectangle:", right(f1, 0.5, 2.3, 10))
print("average rectangle:", aver(f1, 0.59, 2.39, 10))
print("Check:", c1)