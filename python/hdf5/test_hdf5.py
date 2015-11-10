import numpy as np
import h5py
f = h5py.File("test.h5", "w-")
g1 = f.create_group('/Trigonometric_functions')
x = np.linspace(0, np.pi*2, 100)
y1 = np.sin(x)
y2 = np.cos(x)
g1['x'] = x
g1['x'].attrs["Units"] = "meters"
g1['y1'] = y1
g1['y2'] = y2

g2 = f.create_group('/log_func')
g2["x"] = x
g2["y"] = np.log(x)

f.close()
