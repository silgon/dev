import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,5,50)
a = 2
b = 3
y = np.exp(x)/(np.exp(a)+np.exp(b)+np.exp(x))
y_a = np.exp(a)/(np.exp(a)+np.exp(b)+np.exp(x))
y_b = np.exp(b)/(np.exp(a)+np.exp(b)+np.exp(x))

plt.plot(x,y, label="x")
plt.plot(x,y_a, label="a")
plt.plot(x,y_b, label="b")
plt.legend()
plt.show()
