# -*- coding: utf-8 -*-
# author: silgon
# email: silgon3200@gmail.com
from numpy import *
import matplotlib.pylab as plt
from unicycle import Unicycle

# states
t=20
dt=0.01

# person
pz=[1,2,0,1,0,0] 
pz=array(pz)
p= Unicycle(pz,dt)
pzz=array([pz]).T
# robot
rz=[0,0,0,.5,0,0] 
rz=array(rz)
r= Unicycle(rz,dt)
rzz=array([rz]).T

for i in arange(0,t,dt):
    pz[5]+=0.001 # aumenting omega in person
    pdz=p.derivative(pz)
    pz=pz+pdz
    pzz=append(pzz,array([pz]).T,1)
    rdz=p.derivative(rz)
    rz=rz+rdz
    rzz=append(rzz,array([rz]).T,1)

plt.plot(pzz[0,:],pzz[1,:])
plt.plot(rzz[0,:],rzz[1,:])
plt.show()
