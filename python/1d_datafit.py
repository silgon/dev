#! /usr/bin/python
from __future__ import print_function

import numpy as np

# Generate artificial data = straight line with a=0 and b=1
# plus some noise.
xdata= np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
ydata=np.array([0, .5, 1, 1.8, 3, 5, 7, 10, 14])

# Initial guess.
x0    = np.array([0.0, 0.0, 0.0, 0.0])

sigma = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

def func(x, a, b, c, d):
    return a + b*x + c*x**2 + d*x**3

import scipy.optimize as optimization

fitted_x, covar = optimization.curve_fit(func, xdata, ydata, x0, sigma)
print("fitted x:\t", fitted_x, "\ncovariance:\t", covar)

x0=fitted_x

import matplotlib.pyplot as plt
plt.plot(xdata,ydata,'or')
x=np.linspace(0,10)
y=func(x,x0[0],x0[1],x0[2], x0[3])
plt.plot(x,y,'-b')
plt.show()
