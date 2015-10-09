import numpy as np
import matplotlib.pyplot as plt

from hmmlearn import hmm

##############################################################
# Prepare parameters for a 3-components HMM
# Initial population probability
start_prob = np.array([0.6, 0.3, 0.1, 0.0])
# The transition matrix, note that there are no transitions possible
# between component 1 and 4
trans_mat = np.array([[0.7, 0.2, 0.0, 0.1],
                      [0.3, 0.5, 0.2, 0.0],
                      [0.0, 0.3, 0.5, 0.2],
                      [0.2, 0.0, 0.2, 0.6]])
# The means of each component
means = np.array([[0.0,  0.0],
                  [0.0, 11.0],
                  [9.0, 10.0],
                  [11.0, -1.0],
                  ])
# The covariance of each component
covars = .5 * np.tile(np.identity(2), (4, 1, 1))

# Build an HMM instance and set parameters
model = hmm.GaussianHMM(4, "full", start_prob, trans_mat,
                        random_state=42)

# Instead of fitting it from the data, we directly set the estimated
# parameters, the means and covariance of the components
model.means_ = means
model.covars_ = covars
###############################################################

# Generate samples
xdata, y = model.sample(500)

# model2 is used to estimate the values of the real model
model2 = hmm.GaussianHMM(4, "full")
model2.fit([xdata])

print "--real model--\nmean:\n{}\ncovar:\n{}\n\n--fitted model--\nmean:\n{}\ncovar:\n{}".format(\
        model.means_, model.covars_, model2.means_, model2.covars_)
# Plot the sampled data
plt.subplot(1, 3, 1)
plt.title("Samples of real model")
plt.plot(xdata[:, 0], xdata[:, 1], "-o", label="observations", ms=6,
         mfc="orange", alpha=0.7)

# Indicate the component numbers
for i, m in enumerate(means):
    plt.text(m[0], m[1], 'Component %i' % (i + 1),
             size=17, horizontalalignment='center',
             bbox=dict(alpha=.7, facecolor='w'))
plt.legend(loc='best')

# scoring samples and plotting
from sklearn import mixture
MAXS = np.max(means, 0)
MINS = np.min(means, 0)
LIMITS = [MINS[0]-1, MAXS[0]+1, MINS[1]-1, MAXS[1]+1]
x1 = np.linspace(LIMITS[0],  LIMITS[1], 100)
x2 = np.linspace(LIMITS[2],  LIMITS[3], 100)
X1, X2 = np.meshgrid(x1,x2)
xdata = np.array([X1.ravel(), X2.ravel()]).T

# Score samples with GaussianHMM: Frontiers are well defined
Y = model2.score_samples(xdata)
Y = np.max(Y[1], 1).reshape(X1.shape)
plt.subplot(1, 3, 2)
plt.title("Fitted GaussianHMM scores")
plt.pcolormesh(X1, X2, Y)
plt.colorbar()
plt.axis(LIMITS)

# score samples with GMM
mg = mixture.GMM(n_components=4, covariance_type='full')
mg.means_ = model2.means_
mg.covars_ = model2.covars_
Y = -mg.score_samples(xdata)[0]
Y = Y.reshape(X1.shape)
plt.subplot(1, 3, 3)
plt.title("Fitted GMM scores")
CS = plt.contour(X1, X2, Y)
CB = plt.colorbar(CS, shrink=0.8, extend='both')
plt.axis(LIMITS)
plt.plot(model.means_[:,0], model.means_[:,1], 'ob')
plt.plot(model2.means_[:,0], model2.means_[:,1], '^k')
plt.show()
