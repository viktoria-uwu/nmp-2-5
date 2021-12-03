import math  
  
def f(x):  
    return 3*x**4+4*x**3-12*x**2-1  
def pox1(x):  
    return 12*x**3+12*x**2-24*x  
def pox2(x):  
    return 36*x**2+24*x-24  
      
def comb(a, b, e):  
    if(pox1(a)*pox2(a))<0:  
        a0=b 
        b0=a 
    else:  
        a0=a  
        b0=b  
      
    xp1=a0  
    xp2=b0  
      
    xn1=xp1-f(xp1)*(xp2-xp1)/(f(xp2)-f(xp1))  
    xn2=xp2-f(xp2)/pox1(xp2)  
    xp1=xn1  
    xp2=xn2  
      
    while xp2-xp1 > e:  
        xn1=xp1-f(xp1)*(xp2-xp1)/(f(xp2)-f(xp1))  
        xn2=xp2-f(xp2)/pox1(xp2)  
        xp1=xn1  
        xp2=xn2  
      
    x=(xp1+xp2)/2  
     
    return x 
  
print ("Comb method=", comb(-3, -2, 0.0001)) 
print ("Comb method=", comb(1, 2, 0.0001))