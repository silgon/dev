#!/usr/bin/env python
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

# sampling
x = np.linspace(0, 10, 10)
y = np.sin(x)

# spline trough all the sampled points
tck = interpolate.splrep(x, y)
x2 = np.linspace(0, 10, 200)
y2 = interpolate.splev(x2, tck)

# spline with all the middle points as knots (not working yet)
# weights = np.concatenate(([1, .6],np.ones(x.shape[0]-4)*.2,[.2, 1]))
weights = np.ones(x.shape[0])
tck = interpolate.splrep(x, y, w=weights, k=5, s=3)
x3 = np.linspace(0, 10, 200)
y3 = interpolate.splev(x2, tck)

# plot
plt.plot(x, y, 'go', x2, y2, 'b', x3, y3,'r')
plt.show()
