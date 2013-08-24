#!/usr/bin/env python
# generates a file with all random numbers from mini to maxi

import numpy as np

filename="contra"
num_length=10

f = open(filename,'w')
mini=2222222222
maxi=8888888888
i=mini
while i<maxi:
    f.writelines("%d\n" % (i))
    i+=1
    
f.close()

