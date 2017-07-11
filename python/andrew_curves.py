from pandas.tools.plotting import andrews_curves
import pandas as pd
import matplotlib.pyplot as plt

# from sklearn import datasets
# iris = datasets.load_iris()
data = pd.read_csv('iris.data')
andrews_curves(data, 'Name')
plt.show()
