# based on http://www.robots.ox.ac.uk/~mebden/reports/GPtutorial.pdf
import numpy as np
import seaborn as sns
plt = sns.plt

def f(x):
    return x * np.sin(x)
x = np.array([1., 3., 5., 6., 7., 8.]).T
# x = np.atleast_2d([1., 3., 5., 6., 7., 8.]).T
y = f(x).ravel()
# x = np.array([-1.5, -1, -0.75, -0.4, -0.25, 0])
# y = np.array([-1.6, -1.2, -0.5, 0, 0.5, 1])
sigma = 0.3

f_options={
    "1": lambda x_r, x_p: np.exp(-1*np.dot((x_r-x_p),(x_r-x_p))),
    "2": lambda x_r, x_p: np.exp(-1*np.dot((x_r-x_p),(x_r-x_p)))+0.4*(x_r==x_p)
}

kernel = f_options["1"]
Ker = np.zeros((len(x),len(x)))
for i in xrange(len(x)):
    for j in xrange(len(x)):
        Ker[i, j] = kernel(x[i],x[j])

new_x = np.linspace(1, 10, 100)
new_y = np.zeros(len(new_x))
sigma_y = np.zeros(len(new_x))

for i in xrange(len(new_x)):
    x_k = new_x[i]
    Ker_k = [kernel(x_k,x[j]) for j in xrange(len(x))]
    k_k = kernel(x_k,x_k)
    new_y[i] = np.dot(np.dot(Ker_k, np.linalg.inv(Ker)),y)
    sigma_y[i] = k_k - np.dot(np.dot(Ker_k, np.linalg.inv(Ker)), Ker_k)
    # print sigma_y[i],
    sigma_y[i] = sigma_y[i]**.5
    # print ","+str(sigma_y[i])

green = sns.xkcd_rgb["faded green"]
blue = sns.xkcd_rgb["windows blue"]
purple = sns.xkcd_rgb["dusty purple"]
plt.plot(new_x, f(new_x),'--', label="real", color=green)
plt.plot(x, y, 'o', label="samples", color=purple)
plt.plot(new_x, new_y, '-', label="deduced", color=blue)
plt.fill_between(new_x, new_y+sigma_y, new_y-sigma_y, alpha=.5, facecolor=blue)
plt.legend()
plt.show()
