from numpy import *
import matplotlib.pylab as plt
from unicycle import Unicycle

# states
z=[0,0,0,1,0,0]
t=1
dt=0.01
uni= Unicycle(z,dt)
z=array([z]).T
zz=z
for i in arange(0,t,dt):
    dz=uni.derivative(z)
    z=z+dz
    zz=append(zz,z,1)

