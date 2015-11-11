#! /usr/bin/python
"""
This example creates an HDF5 playing around with properties and lastly
creating an compound database
"""
import numpy as np
import h5py

# @write
FILENAME = "test.h5"
f = h5py.File("test.h5", "w")
g1 = f.create_group('/Trigonometric_functions')
x = np.linspace(0, np.pi*2, 100)
y1 = np.sin(x)
y2 = np.cos(x)
g1['x'] = x
g1['x'].attrs["Units"] = "meters"
g1['y1'] = y1
g1['y2'] = y2

g2 = f.create_group('/compressed')
g2.create_dataset('x', data=x, compression="gzip")
g2.create_dataset('y', data=np.exp(x), compression="gzip")

g3 = f.create_group('/all_in_one')
data = np.array([x,y1, y2]).T
g3_dset=g3.create_dataset('data', data=data, compression="gzip")
g3_dset.attrs['column_names'] = ['x', 'sin', 'cos']
g3_dset.attrs['columns'] = ['x', 'sin', 'cos']

# compound
comp_type = np.dtype([('x', np.float), ('sin', np.float), ('sin^2', np.float), ('cos', np.float)])
cdata = np.zeros(x.shape, dtype=comp_type)
cdata['x'] = x
cdata['sin'] = y1
cdata['sin^2'] = np.sin(x)**2
cdata['cos'] = y2
g3_dset=g3.create_dataset('cdata', data=cdata, compression="gzip")

f.close()

# @read
f = h5py.File("test.h5", "r")
dset = f['/all_in_one']
data1 = dset['data'].value  # all in one
data2 = dset['cdata'].value  # compound
f.close()
# plot
import seaborn as sns
plt = sns.plt
plt.figure(0)
plt.plot(data1[:,0], data1[:,1], '-', data1[:,0], data1[:,2], '--')
plt.figure(1)
plt.plot(data2['x'], data2['sin'], '-', data2['x'], data2['sin^2'], '--')

plt.figure(0)

plt.show()
