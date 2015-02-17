import numpy as np
import matplotlib.pyplot as plt

mu_x = 0
mu_y = 0

sig_rx = 2
sig_lx = .5
sig_y = 2

side = np.arange(-5, 5, .05)
X, Y = np.meshgrid(side, side)
Z = np.exp(-((X-mu_x)**2/(2*np.where(X > mu_x, sig_rx, sig_lx)**2)
             +(Y-mu_y)**2/(2*np.where(X > mu_x, sig_y, sig_y)**2)))

plt.pcolormesh(X, Y, Z)
plt.colorbar()
plt.show()
