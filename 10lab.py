import matplotlib.pyplot as plt
from numpy import *
from scipy.interpolate import UnivariateSpline

x = [1, 1.3, 1.7, 2.2, 2.8]
y = [2.95, 3.89, 1.46, 3.38, 2.34]

spl = UnivariateSpline(x,y)
xs = linspace(-5, 10, 1000)

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline Interpolation')
plt.plot(x, y, 'ro' , xs, spl(xs), 'b' )
plt.show()