from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
Nsteps, Nwalkers = 1000, 250
t = np.arange(Nsteps)

np.random.seed(0)
# an (Nsteps x Nwalkers) array of random walk steps
S1 = 0.002 + 0.01*np.random.randn(Nsteps, Nwalkers)
S2 = 0.004 + 0.02*np.random.randn(Nsteps, Nwalkers)

# an (Nsteps x Nwalkers) array of random walker positions
X1 = S1.cumsum(axis=0)
X2 = S2.cumsum(axis=0)


# Nsteps length arrays empirical means and standard deviations of both
# populations over time
mu1 = X1.mean(axis=1)
sigma1 = X1.std(axis=1)
mu2 = X2.mean(axis=1)
sigma2 = X2.std(axis=1)
# plot it!
plt.plot(t, mu1, lw=2, label='mean population 1', color='blue')
plt.fill_between(t, mu1+sigma1, mu1-sigma1, facecolor='blue', alpha=0.5)
plt.plot(t, mu2, lw=2, label='mean population 2', color='yellow')
plt.fill_between(t, mu2+sigma2, mu2-sigma2, facecolor='yellow', alpha=0.5)
plt.title('random walkers empirical $\mu$ and $\pm \sigma$ interval')
plt.legend(loc='upper left')
plt.xlabel('num steps')
plt.ylabel('position')
plt.grid()
plt.show()

