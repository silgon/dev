from __future__ import print_function
import numpy as np

gmap = np.random.randint(0, 4, (10, 10))

x_size, y_size = gmap.shape
n_states = np.prod(gmap.size)
successors = np.zeros((n_states, 8))

k = 0
for i in range(x_size):
    for j in range(y_size):
        # current # gmap[i,j]
        # top
        successors[k, 0] = gmap[i, j+1]
        # top right
        successors[k, 1] = gmap[i+1, j+1] * 2**.5
        # right
        successors[k, 2] = gmap[i+1, j]
        # bottom right
        successors[k, 3] = gmap[i+1, j-1] * 2**.5
        # bottom
        successors[k, 4] = gmap[i, j-1]
        # bottom left
        successors[k, 5] = gmap[i-1, j-1] * 2**.5
        # left
        successors[k, 6] = gmap[i-1, j]
        # top left
        successors[k, 7] = gmap[i-1, j+1] * 2**.5
        k += 1
