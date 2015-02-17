import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return np.sin(x)
x = y = np.arange(-3,3,.05)
X, Y = np.meshgrid(x, y)
Z = Y**2+X**2

gy,gx = np.gradient(Z,.05,.05)
plt.subplot(2,2,1)
plt.pcolormesh(X, Y, Z)
plt.subplot(2,2,2)
plt.quiver(X,Y,gy,gx)
plt.subplot(2,2,3)
plt.pcolormesh(X, Y, gx)
plt.subplot(2,2,4)
plt.pcolormesh(X, Y, gy)

plt.show()

