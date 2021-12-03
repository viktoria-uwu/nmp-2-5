import numpy as np  
import matplotlib.pyplot as plt  
from scipy.interpolate import lagrange  
   
   
x=np.array([-3,-1,0,2], dtype=float)  
y=np.array([-16, 14, -2, 4], dtype=float)  
def lag(x,y,t):  
   b=0  
   for k in range(len(y)):  
       p1=1; p2=1  
       for i in range(len(x)):  
           if i==k:  
               p1=p1*1; p2=p2*1  
           else:  
               p1=p1*(t-x[i])  
               p2=p2*(x[k]-x[i])  
       b=b+y[k]*p1/p2  
   return b  
graphX=np.linspace(np.min(x),np.max(x),100)  
graphY=[lag(x,y,i) for i in graphX]  
plt.plot(x,y,'bo',graphX,graphY)  
plt.grid() 
plt.legend(['(16x^3+33x^2-31x-6)/3'], loc = 'upper right') 
plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y') 
plt.show() 
 
n = 3  
yp = 0 
x1 = -2 
for i in range(len(x)): 
 p = 1 
 for j in range(len(y)): 
  if i != j: 
   p = p * (x1-x[j])/(x[i]-x[j]) 
 yp=yp+p*y[i] 
print('interpolit value at ', x1, ' = ', yp) 
 
 
x2 = -1.5 
 
for i in range(len(x)): 
 p = 1 
 for j in range(len(y)): 
  if i != j: 
   p = p * (x2-x[j])/(x[i]-x[j]) 
 yp=yp+p*y[i] 
print('interpolit value at ', x2, ' = ', yp) 
 
x3 = -0.5 
 
for i in range(len(x)): 
 p = 1 
 for j in range(len(y)): 
  if i != j: 
   p = p * (x3-x[j])/(x[i]-x[j]) 
 yp=yp+p*y[i] 
print('interpolit value at ', x3, ' = ', yp) 
 
x4 = 1 
 
for i in range(len(x)): 
 p = 1 
 for j in range(len(y)): 
  if i != j: 
   p = p * (x4-x[j])/(x[i]-x[j]) 
 yp=yp+p*y[i] 
print('interpolit value at ', x4, ' = ', yp) 
 
f = lagrange(x, y) 
fgr = plt.figure(figsize = (10, 8)) 
plt.plot(x,y,'go',graphX,graphY)  
plt.grid() 
plt.legend(['(16x^3+33x^2-31x-6)/3'], loc = 'upper right') 
plt.title('Shvets') 
plt.xlabel('x(check)') 
plt.ylabel('y(check)') 
 
 
plt.show()