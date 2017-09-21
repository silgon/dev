from scipy.stats import powerlaw
import matplotlib.pyplot as plt
import numpy as np

pl=powerlaw(.8, loc=0, scale=2)
samples = pl.rvs(10000) # create random variables
alpha, loc, scale = powerlaw.fit(samples) # fit the variables

# plotting
plt.figure(0)
plt.clf()
plt.hist(samples, bins=50, normed=True, histtype='stepfilled', alpha=.9)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
plt.plot(x, pl.pdf(x), linewidth=2, label="fit")

plt.figure(1)
plt.clf()
plt.hist(samples, bins=50, normed=True, histtype='stepfilled', alpha=.9)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
plt.plot(x, pl.pdf(x), linewidth=2, label="fit")
plt.xscale("log", basex=10,nonposy='clip')
plt.yscale("log", basey=10,nonposy='clip')

plt.show()
