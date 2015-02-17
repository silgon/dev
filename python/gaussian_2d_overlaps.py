import numpy as np
import matplotlib.pyplot as plt

sig_rx = 2
sig_lx = 1
sig_y = 2

step = .1
side = np.arange(-10, 10, step)
size = len(side)
X_base, Y_base = np.meshgrid(side, side)
def proxemics(x=0, y=0, th=0):
    """Proxemics mapping of one person with 2 gaussians (front and back)
    variables are position and orientation of this person
    """
    # a = np.cos(th)**2/2/sig_rx**2 + np.sin(th)**2/2/sig_y**2
    # b = -np.sin(2*th)/4/sig_rx**2 + np.sin(2*th)/4/sig_y**2
    # c = np.sin(th)**2/2/sig_rx**2 + np.cos(th)**2/2/sig_y**2
    # Z = np.exp(-(a*(X-x)**2 + 2*b*(X-x)*(Y-y) + c*(Y-y)**2))
    # Rotation
    X_tmp = np.reshape(X_base,(size*size))
    Y_tmp = np.reshape(Y_base,(size*size))
    tmp = np.dot(rot(th), np.array([X_tmp, Y_tmp]))
    X = np.reshape(tmp[0,:], (size, size))
    Y = np.reshape(tmp[1,:], (size, size))
    
    Z = np.exp(-((X-x)**2/(2*np.where(X > x, sig_rx, sig_lx)**2)
             +(Y-y)**2/(2*np.where(X > x, sig_y, sig_y)**2)))
    return Z

def rot(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])


# Function for every point
Z1 = proxemics(2,2, np.pi)
Z2 = proxemics(-2,2, 0)
Z3 = proxemics(0,2, np.pi/2.)

# Sum
Z = Z1+Z2+Z3
plt.subplot(2,2,1)
plt.title("Sum")
plt.pcolormesh(X_base, Y_base, Z)
plt.colorbar()

# Gradients
plt.subplot(2,2,2)
plt.title("Gradient Quiver")
gy,gx = np.gradient(Z, step, step)
plt.quiver(X_base, Y_base, gy, gx)

# x-gradient
plt.subplot(2,2,3)
plt.title("Gradient x axis")
plt.pcolormesh(X_base, Y_base, gx)
plt.colorbar()
# y-gradient
plt.subplot(2,2,4)
plt.title("Gradient y axis")
plt.pcolormesh(X_base, Y_base, gy)
plt.colorbar()

plt.show()
