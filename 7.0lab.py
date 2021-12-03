from numpy import *
import matplotlib.pyplot as plt

x = linspace(1, 3, 51)
y = 5*tan(x)*exp(x**2+1/x)
plt.plot(x, y, 'bo-')
plt.xlabel('x')  
plt.ylabel('y') 
plt.title('F(x)')  
plt.legend(['5*tan(x)*exp(x^2+1/x),'], loc = 'upper right')
plt.grid()
plt.show()