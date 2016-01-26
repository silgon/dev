#! /usr/bin/python
import numpy as np
import seaborn as sns
plt = sns.plt

# sig_x_front = 2
# sig_x_back = 1
# sig_y_sides = 2
sig_x = 4
sig_y = 2
theta= np.pi/6
mu_x = 0
mu_y = 0

X, Y = np.meshgrid(np.arange(-10,10,0.1),
                   np.arange(-10,10,0.1));


a = np.cos(theta)**2/(2*sig_x**2) + np.sin(theta)**2/(2*sig_y**2)
b = -np.sin(2*theta)/(4*sig_x**2) + np.sin(2*theta)/(4*sig_y**2)
c = np.sin(theta)**2/(2*sig_x**2) + np.cos(theta)**2/(2*sig_y**2)

Z = np.exp(-(a*(X-mu_x)**2 - 2*b*(X-mu_x)*(Y-mu_y) + c*(Y-mu_y)**2))

plt.contour(X, Y, Z, cmap="viridis")
plt.show()
