from numpy import *
import matplotlib.pylab as plt
from unicycle import Unicycle

# states
z=[0,0,0,1,0,0]
t=20
dt=0.01

z=array(z)
uni= Unicycle(z,dt)
zz=array([z]).T
for i in arange(0,t,dt):
    z[5]+=0.001
    dz=uni.derivative(z)
    z=z+dz
    zz=append(zz,array([z]).T,1)
plt.plot(zz[0,:],zz[1,:])
plt.show()
