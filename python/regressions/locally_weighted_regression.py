#! /usr/bin/python
"""
Linear Regression based on:
http://vilkeliskis.com/blog/2013/09/08/machine_learning_part_2_locally_weighted_linear_regression.html
"""
import numpy as np
from sklearn import linear_model
import seaborn as sns
plt = sns.plt

def gaussian_kernel(x, x0, c, a=1.0):
    """
    Gaussian kernel.

    :Parameters:
      - `x`: nearby datapoint we are looking at.
      - `x0`: data point we are trying to estimate.
      - `c`, `a`: kernel parameters.
    """
    # Euclidian distance
    diff = x - x0
    dot_product = diff * diff.T
    return a * np.exp(dot_product / (-2.0 * c**2))


def get_weights(training_inputs, datapoint, c=1.0):
    """
    Function that calculates weight matrix for a given data point and training
    data.

    :Parameters:
      - `training_inputs`: training data set the weights should be assigned to.
      - `datapoint`: data point we are trying to predict.
      - `c`: kernel function parameter

    :Returns:
      NxN weight matrix, there N is the size of the `training_inputs`.
    """
    x = np.mat(training_inputs)
    n_rows = x.shape[0]
    # Create diagonal weight matrix from identity matrix
    weights = np.mat(np.eye(n_rows))
    for i in xrange(n_rows):
        weights[i, i] = gaussian_kernel(datapoint, x[i], c)
    return weights


def lwr_predict(training_inputs, training_outputs, datapoint, c=1.0):
    """
    Predict a data point by fitting local regression.

    :Parameters:
      - `training_inputs`: training input data.
      - `training_outputs`: training outputs.
      - `datapoint`: data point we want to predict.
      - `c`: kernel parameter.

    :Returns:
      Estimated value at `datapoint`.
    """
    weights = get_weights(training_inputs, datapoint, c=c)
    x = np.mat(training_inputs)
    y = np.mat(training_outputs).T
    xt = x.T * (weights * x)
    betas = xt.I * (x.T * (weights * y))
    return datapoint * betas

data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
data_shape = data.shape
inputs = np.array([np.ones(data.shape[0]), data[:, 1]]).T
outputs = data[:, 0]

test_x = np.arange(np.min(data[:, 1]), np.max(data[:, 1]), 0.02)

predictions01 = []
predictions02 = []
predictions1 = []
for item in test_x:
    res01 = lwr_predict(inputs, outputs, [1, item], c=0.1).A.flatten()[0]
    res02 = lwr_predict(inputs, outputs, [1, item], c=0.2).A.flatten()[0]
    res1 = lwr_predict(inputs, outputs, [1, item], c=1).A.flatten()[0]
    predictions01.append(res01)
    predictions02.append(res02)
    predictions1.append(res1)

plt.plot(test_x, predictions01)
plt.plot(test_x, predictions02)
plt.plot(test_x, predictions1)
plt.plot(inputs[:, 1], outputs, 'o')
plt.show()
