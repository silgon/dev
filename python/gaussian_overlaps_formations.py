import numpy as np
import matplotlib.pyplot as plt

sig_x_front = 1
sig_x_back = .5
sig_y_sides = .5
mu_x = 0
mu_y = 0
sigma = (.2, .2, .2)

def proxemics(position=(0, 0, 0)):
    """Proxemics mapping of one person with 2 gaussians (front and back)
    variables are position and orientation of this person
    """
    x, y, th = position
    # reshape base values
    X_tmp = np.reshape(X_base,(size_x*size_y))
    Y_tmp = np.reshape(Y_base,(size_x*size_y))
    # translate and rotate matrix
    tmp = np.dot(rot(-th), np.array([X_tmp - x, Y_tmp - y]))
    # reshape
    X = np.reshape(tmp[0,:], (size_y, size_x))
    Y = np.reshape(tmp[1,:], (size_y, size_x))
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
                      theta+np.pi*(1+i*2./n)+sg_th])

poses = []
center = (2, 2, 0)
circleFormation(4, poses, center, .6)
# get min-max for the poses
mpos = np.array(poses)
min_x, min_y, min_th = np.min(mpos, 0)
max_x, max_y, max_th = np.max(mpos, 0)

# parameters of the grid
step = .2
margin = 2.5
side_x = np.arange(min_x-margin, max_x+margin, step)
side_y = np.arange(min_y-margin, max_y+margin, step)
size_x = len(side_x)
size_y = len(side_y)
X_base, Y_base = np.meshgrid(side_x, side_y)

# Function for every point
for i in xrange(len(poses)):
    if i==0:
        Z = proxemics(poses[i])
    else:
        Z += proxemics(poses[i])

# plot vectors
pi_x, pi_y, pi_th = zip(*poses)
pe_x, pe_y = .5*np.cos(pi_th), .5*np.sin(pi_th)
plt.figure(0)
plt.title("Poses")
plt.quiver(pi_x, pi_y, pe_x, pe_y, angles='xy',
           scale_units='xy', scale=1, linewidth=1)
plt.axis([min_x-1,max_x+1,min_y-1,max_y+1])

plt.figure(1)
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
