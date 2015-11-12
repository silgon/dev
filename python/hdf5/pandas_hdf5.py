#! /usr/bin/python
"""
This example reads with pandas an HDF5 file
"""
import numpy as np
import pandas as pd
import h5py
FILENAME = "test_pandas.h5"

def df_to_sarray(df):
    """
    Convert a pandas DataFrame object to a numpy structured array.
    This is functionally equivalent to but more efficient than
    np.array(df.to_array())

    :param df: the data frame to convert
    :return: a numpy structured array representation of df
    """

    v = df.values
    cols = df.columns
    types = [(cols[i].encode(), df[k].dtype.type) for (i, k) in enumerate(cols)]
    dtype = np.dtype(types)
    z = np.zeros(v.shape[0], dtype)
    for (i, k) in enumerate(z.dtype.names):
        z[k] = v[:, i]
    return z

df = pd.DataFrame(np.random.rand(50,3), columns=list("ABC"))

f = h5py.File(FILENAME, "w")
g1 = f.create_group('/g1')
g1.create_dataset('data', data=df_to_sarray(df), compression="gzip")

f.close()

data = pd.read_hdf(FILENAME, '/g1/data')
print data
