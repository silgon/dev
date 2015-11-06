#! /usr/bin/python
"""
Linear Regression based on:
http://vilkeliskis.com/blog/2013/08/14/machine_learning_part_1_linear_regression.html
"""
import numpy as np
from sklearn import linear_model
import seaborn as sns
plt = sns.plt

def fit(inputs, outputs):
    """
    Solve a set of linear regression equations for betas using linear algebra.
    :Parameters:
      - `inputs`: array-like
      - `outputs`: array-like
    """
    return np.dot(np.linalg.pinv(inputs), outputs)

data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
data_shape = data.shape
inputs = np.array([np.ones(data.shape[0]), data[:, 1]]).T
outputs = data[:, 0]
ls_coef_ = fit(inputs, outputs)  # least squares coefficients

model = linear_model.LinearRegression(fit_intercept=False)
model.fit(inputs, outputs)

print "Values of least squares fit: {}".format(ls_coef_)
print "Values of Linear Regression: {}".format(model.coef_)

# display points
plt.plot(inputs[:,1], outputs, 'o')

# display fitted lines
x = np.linspace(2, 5 , 100)
y1 = ls_coef_[0] + ls_coef_[1]*x
y2 = model.coef_[0] + model.coef_[1]*x
plt.plot(x, y1, '-', x, y2, '--')

plt.show()
