#! /usr/bin/python
import yaml
filename = open('test.yaml')
data = yaml.safe_load(filename)
import numpy as np
print np.array(data['array'])
