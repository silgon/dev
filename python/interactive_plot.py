#! /usr/bin/python
import time
import numpy as np
import matplotlib.pyplot as plt

plt.ion()
plt.show()
# plt.hold(True)
plt.figure(0)
for i in xrange(1000):
    plt.clf()
    x = np.linspace(i/50.,i/50.+5,100)
    y = np.sin(x)
    plt.plot(x,y,'b')
    plt.draw()
    time.sleep(0.05)
    plt.pause(0.0001)
