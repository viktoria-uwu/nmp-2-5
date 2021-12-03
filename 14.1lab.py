import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def f(x,y):
    return x+cos(y/sqrt(1.3))
  
x0=1.2
p=2.1
h=0.1
x=np.arange(x0,p+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=1.8

for i in range(n):
    y[i+1]=y[i]+f(x[i],y[i])*h

print('xi=',x)
print('yi=',y)

plt.plot(x, y,'ko-')
plt.xlabel('x') 
plt.ylabel('y')
plt.title('Euler method') 
plt.legend(['x+cos(y/sqrt(1,3))'])
plt.grid()
plt.show()