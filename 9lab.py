import numpy as np
import matplotlib.pyplot as plt
from math import factorial

x = np.array([0, 0.2,0.4,0.6,0.8, 1])
y =np.array([1.2715, 2.4652,3.6443,4.8095,5.9614,7.1005])
x1=0.1
x2 = 0.9
h = x[1] - x[0]
q = (x1 - 0)/h
q1 = (x2 - 1)/h

def f( y, j):
    mas = []

    for i in range(len(y)):
        mas.append(y[i]-y[i-1])
    mas.pop(0)

    if j==1:
        return mas
    else:
        j -=1 
        return f(mas,j)

yx1= y[0] - q1*(f(y, 1)[0]) + (q1*(q1-1)/factorial(2))*(f(y, 2)[0]) + (q1*(q1-1)*(q1-2)/factorial(3))*(f(y, 3)[0])+(q1*(q1-1)*(q1-2)*(q1-4)/factorial(4))*(f(y, 4)[0])+(q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)/factorial(5))*(f(y, 5)[0])
yx2= y[5] - q*(f(y, 1)[4]) + (q*(q-1)/factorial(2))*(f(y, 2)[3]) + (q*(q-1)*(q-2)/factorial(3))*(f(y, 3)[2])+(q*(q-1)*(q-2)*(q-4)/factorial(4))*(f(y, 4)[1])+(q*(q-1)*(q-2)*(q-3)*(q-4)/factorial(5))*(f(y, 5)[0])
print(f(y, 1))