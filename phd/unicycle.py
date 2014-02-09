# -*- coding: utf-8 -*-
__author__ = ['silgon']

from numpy import *
# import matplotlib.pylab as plt

class Unicycle():
    """This is the model of the unicycle we're simulating
    """
    
    def __init__(self, z,dt=0.01):
        """
        
        Arguments:
        - `z`: x, y, th, dx, dy, dth
        - `dt`: timestep
        """
        self._z=z
        self._dt=dt
    def derivative(self,z):
        """ set the 
        """
        x=z[0]
        y=z[1]
        th=z[2]
        dx=z[3]
        dy=z[4]
        dth=z[5]
        dt=self._dt
        return array([dx*cos(th)*dt,dx*sin(th)*dt,dth*dt,0,0,0]).T
