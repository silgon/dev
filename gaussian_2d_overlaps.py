import numpy as np
import matplotlib.pyplot as plt

sig_rx = 2
sig_lx = 1
sig_y = 2

side = np.arange(-10, 10, .05)
X, Y = np.meshgrid(side, side)
def proxemics(x=0, y=0, th=0):
    """Proxemics mapping of one person with 2 gaussians (front and back)
    variables are position and orientation of this person
    """
    a = np.cos(th)**2/2/sig_rx**2 + np.sin(th)**2/2/sig_y**2
    b = -np.sin(2*th)/4/sig_rx**2 + np.sin(2*th)/4/sig_y**2
    c = np.sin(th)**2/2/sig_rx**2 + np.cos(th)**2/2/sig_y**2
    Z = np.exp(-(a*(X-x)**2 + 2*b*(X-x)*(Y-y) + c*(Y-y)**2))
    # Z = np.exp(-((X-x)**2/(2*np.where(X > x, sig_rx, sig_lx)**2)
    #          +(Y-y)**2/(2*np.where(X > x, sig_y, sig_y)**2)))
    return Z
Z = proxemics()
plt.pcolormesh(X, Y, Z)
plt.colorbar()
plt.show()
