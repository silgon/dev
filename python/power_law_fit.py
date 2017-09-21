from scipy.stats import powerlaw
import matplotlib.pyplot as plt
import numpy as np

pl=powerlaw(.3, loc=0.3, scale=2)
samples = pl.rvs(10000) # create random variables
alpha, loc, scale = powerlaw.fit(samples) # fit the variables
