import math 
from scipy import optimize

x0 = 0 
y0 = 0.6 

def hybrid(x):
    return math.sin(x[1]+1)-x[0]-1, 2*x[1]+math.cos(x[0])-2
solve = optimize.root(hybrid, [0,0], method = 'hybr')
 
def f1(y): 
    return -1+math.sin(y+1) 
def f2(x): 
    return 1-(math.cos(x)/2) 
 
def simple(x, y, e): 
    xn = x 
    yn = y 
    xn1 = f2(x) 
    yn1 = f1(y) 
    n = 1 
    while((abs(xn1 - xn) >= e) & (abs(yn1 - yn) >= e)): 
        xn = xn1 
        yn = yn1 
        xn1 = f2(yn) 
        yn1 = f1(xn1) 
        n = n + 1 

    print('Method hybrid iteration:', solve.x)
    print('Method of simple iteration:','[', xn, ' ', yn1,']', '\nNumber of iteration = ', n) 
simple(x0, y0, 0.0001)