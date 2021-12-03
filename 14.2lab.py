import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def f(x,y):
 return x+sin(y/sqrt(1.25))
x0=0.5
p=1.5
h=0.1
x=np.arange(x0,p+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=1.8
for i in range(n):
    y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i]+h*f(x[i],y[i])))*h/2

print('xi=',x)
print('yi=',y)
plt.plot(x, y,'ko-')
plt.xlabel('x') 
plt.ylabel('y')
plt.title('Method Euler-Koshi') 
plt.legend(['x+sin(y/sqrt(1.25))'])
plt.grid()
plt.show()