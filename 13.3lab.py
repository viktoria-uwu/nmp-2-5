import math
from numpy import *
from scipy import integrate
def f3(x):
    return 1 / sqrt(2 * x**2 + 1.3)

def trap(f3, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f3(a) + f3(b))
    
    for i in range(1, n):
        sum += f3(a + i * h)
    return sum * h

c3, err = integrate.quad(f3, 1, 2)
print("Trapezoidal method:", trap(f3, 1, 2, 20))
print("Check:", c3)