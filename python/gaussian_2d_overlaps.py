import numpy as np
import matplotlib.pyplot as plt

sig_x_front = 2
sig_x_back = 1
sig_y_sides = 2
mu_x = 0
mu_y = 0

step = .1
side = np.arange(-10, 10, step)
size = len(side)
X_base, Y_base = np.meshgrid(side, side)
def proxemics(x=0, y=0, th=0):
    """Proxemics mapping of one person with 2 gaussians (front and back)
    variables are position and orientation of this person
    """
    # reshape base values
    X_tmp = np.reshape(X_base,(size*size))
    Y_tmp = np.reshape(Y_base,(size*size))
    # translate and rotate matrix
    tmp = np.dot(rot(-th), np.array([X_tmp - x, Y_tmp - y]))
    # reshape
    X = np.reshape(tmp[0,:], (size, size))
    Y = np.reshape(tmp[1,:], (size, size))
    # calculate gaussian
    Z = np.exp(-((X-mu_x)**2/(2*np.where(X > mu_x, sig_x_front, sig_x_back)**2)
             +(Y-mu_y)**2/(2*np.where(X > mu_x, sig_y_sides, sig_y_sides)**2)))
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
# Z = proxemics(2,2,0)+proxemics(-2,-2,np.pi)
plt.subplot(2,2,1)
plt.title("Sum")
plt.pcolormesh(X_base, Y_base, Z)
plt.colorbar()

# Gradients
plt.subplot(2,2,2)
plt.title("Gradient Quiver")
gy,gx = np.gradient(Z, step, step)
plt.quiver(X_base, Y_base, gy, gx)

# mu_x-gradient
plt.subplot(2,2,3)
plt.title("Gradient mu_x axis")
plt.pcolormesh(X_base, Y_base, gx)
plt.colorbar()
# mu_y-gradient
plt.subplot(2,2,4)
plt.title("Gradient mu_y axis")
plt.pcolormesh(X_base, Y_base, gy)
plt.colorbar()

plt.show()
