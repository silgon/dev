import numpy as np
import matplotlib.pyplot as plt

sig_x_front = 1
sig_x_back = .5
sig_y_sides = 1
mu_x = 0
mu_y = 0
sigma = (.2, .2, .2)

step = .1
side = np.arange(-10, 10, step)
size = len(side)
X_base, Y_base = np.meshgrid(side, side)
def proxemics(position=(0, 0, 0)):
    """Proxemics mapping of one person with 2 gaussians (front and back)
    variables are position and orientation of this person
    """
    x, y, th = position
    # reshape base values
    X_tmp = np.reshape(X_base,(size*size))
    Y_tmp = np.reshape(Y_base,(size*size))
    # translate and rotate matrix
    tmp = np.dot(rot(th), np.array([X_tmp - x, Y_tmp - y]))
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

def circleFormation(n, poses, center, radius):
    x, y, theta = center
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    r = radius
    for i in xrange(n):
        poses.append([x+r*np.cos(theta+i*2*np.pi/n+sg_x),
                      y+r*np.sin(theta+i*2*np.pi/n+sg_y),
                      theta+np.pi*(1-i*2./n)+sg_th])

poses = []
center = (0, 0, 0)
circleFormation(4, poses, center, 2)

# Function for every point
for i in xrange(len(poses)):
    if i==0:
        Z = proxemics(poses[i])
    else:
        Z += proxemics(poses[i])

# Sum
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
