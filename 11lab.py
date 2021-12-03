import matplotlib.pyplot as plt
from numpy import *
import math

def fun(x):
  # x**2*sin(x) - function
  f = x**3
  return f

x = linspace(-5, 5, 1000)
y = x**2*sin(x)
yx = fun(x)


plt.plot(x, y, label='x^2*sin(x)')
plt.plot(x, yx, label='x^3')
plt.legend()
plt.title('Taylor Expansion')
plt.grid()
plt.show()


# pox1 = x**2*cos(x) + 2*x*sin(x)
# pox2 = -x**2*sin(x) + 4*x*cos(x) + 2*sin(x)
# pox3 = -x**2*cos(x) - 6*x*sin(x) + 6*x*cos(x)