#! /usr/bin/python
import numpy as np
import yaml
filename = open('test.yaml', "w")
data = {'number': 3, 2: 1, 'string': "on earth", 'array': np.diag([3, 4, 6, 7]).tolist()}
yaml.dump(data, filename)
