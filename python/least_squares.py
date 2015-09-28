"""
Basic Least Squares Implementation with pseudo inverse
"""
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

t = np.linspace(0, 3, 20)  # horizontal axis
x = np.array([3, 0, 4])  # a,b,c  of f(t)=a+b*t+c*t^2
f = lambda t, x: x[0]+x[1]*t+x[2]*t**2  # f(t)
# apply function
y = f(t, x)
# adding noise
noise_factor = 2
noise = np.random.randn(t.shape[0])* noise_factor
y_noise = y + noise

# construct A matrix
f2 = lambda t: np.array([[1]*len(t), t, t**2]).T
A = f2(t)

# Least Squares x=inv(A)y
new_x = np.dot(np.linalg.pinv(A), y_noise)
# apply new values
new_y = f(t, new_x)
print "real values: {}\n noise: {}\n least squares: {}".format(x, noise_factor, new_x)
plt.plot(t,y,'-b', label="perfect function")
plt.plot(t,y_noise,'or', label="function with noise")
plt.plot(t,new_y,'--k', label="least squares")
plt.legend(loc='upper left')
plt.show()
