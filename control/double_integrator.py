#! /usr/bin/python
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0, 1], [0, 0]])
B = np.array([[0, 1]]).T
k1 = 40
k2 = 10
K = np.array([[-k1, -k2]])
x0 = np.array([[0, 0]]).T
x_goal = np.array([[5, 0]]).T
dt = .01

x_t = x0
err = x_goal - x_t
t = 0
T = [t]
Xs = [x_t.T[0]]
Err = [err.T[0]]
# while err[0] > .1:
for i in xrange(1000):
    err = x_goal - x_t
    x_t = x_t + (np.dot(A, x_t) - np.dot(B, np.dot(K, err)))*dt
    Xs.append(x_t.T[0])
    Err.append(err.T[0])
    T.append(T[-1]+dt)

Xs = np.array(Xs)
Err = np.array(Err)
T = np.array(T)
plt.plot(T, Xs[:,0], label="position")
plt.plot(T, Xs[:,1], label="velocity")
plt.legend()
plt.show()

