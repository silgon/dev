#! /usr/bin/python
"""
This example creates an HDF5 file compound.h5 and an empty datasets /DSC in it.
"""

# write
import h5py
import numpy as np
FILENAME = "compound.h5"
file = h5py.File(FILENAME,'w')

comp_type = np.dtype([('Orbit', 'i'), ('Location', np.str_, 6), ('Temperature (F)', 'f8'), ('Pressure (inHg)', 'f8')])
data = np.array([(1153, "Sun   ", 53.23, 24.57), (1184, "Moon  ", 55.12, 22.95), (1027, "Venus ", 103.55, 31.23), (1313, "Mars  ", 1252.89, 84.11)], dtype = comp_type)

# dataset = file.create_dataset("DSC",(4,), comp_type)
# dataset[...] = data
dataset = file.create_dataset("DSC",data=data)
file.close()

# read 
file = h5py.File(FILENAME, 'r')
dataset = file["DSC"]
print "Reading Orbit and Location fields..."
orbit = dataset['Orbit']
print "Orbit: ", orbit
location = dataset['Location']
print "Location: ", location
data = dataset[...]
print "Reading all records:"
print data
print "Second element of the third record:", dataset[2, 'Location']
file.close()
