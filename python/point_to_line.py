import numpy as np
import seaborn as sns
plt = sns.plt

p = [2., -4.]
# ax+by+c=0
a = 4.
b = 2.
c = 2.
result = abs(a*p[0]+b*p[1]+c)/np.sqrt(a**2+b**2)
print(result)

# y = -bx-c
bb = a/b
cc = c/b
result2 = abs(p[0]*bb+p[1]+cc)/np.sqrt(1+bb**2)
print(result2)

x = np.linspace(0, 10, 50)
y = -bb*x-cc
plt.plot(x, y)
plt.plot(p[0], p[1], 'o')
plt.show()
