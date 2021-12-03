import math
from numpy import *
from scipy import integrate

def f2(x):
    return (x/2+1)*sin(x/2)

def simpson(a, b, n):
    h = (b - a) / n
    integration = f2(a) + f2(b)

    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            integration = integration + 2 * f2(k)
        else:
            integration = integration + 4 * f2(k)

    integr = integration * h / 3
    return integr

c2, err = integrate.quad(f2, 1.2, 2.8)
print("Simpsone method:", simpson(1.2, 2.8, 8))
print("Check:", c2)