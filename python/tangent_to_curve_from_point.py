# Step 1 : we start with point P(x_0,y_0)

#Step 2: We define our function and compute the derivative
# y = 2*x^2
# y' = 4x

# Step 3
# equation of the line given a point
# y_0-y = m(x_0-x)
# where m = y' = 4x thus
# y_0-y = 4x(x_0-x)
# we replace y
# y_0 - 2*x^2 = 4x(x_0-x)
# we order it as in a quadratic equation
# -2*x^2+4*x*x_0-y_0 = 0
# we solve for x = (-b ± sqrt(b^2-4ac))/(2a) where a=-2, b=4*x_0, c=-y_0
# solve for y = 2*x^2

# Step 4:
# let's say we have two our solutions (x_1,y_1) and (x_2,y_2)
# from  y-y_1 = 4*x_1(x-x_1)
# then you'll have your two tangent lines
# y = 4*x_1*x-4*x_1^2+y_1
# y = 4*x_2*x-4*x_2^2+y_2

# curve
import numpy as np
import matplotlib.pyplot as plt

# Step 1
p = (-1,-2)
x_0 = p[0]
y_0 = p[1]

# Step 2
x = np.linspace(-3,3,100)
y = 2*x**2

# Step 3
a,b,c=-2,4*x_0,-y_0
x_1 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
y_1 = 2*x_1**2
x_2 = (-b-np.sqrt(b**2-4*a*c))/(2*a)
y_2 = 2*x_2**2

# Step 4
ty_1 = 4*x*x_1+y_1-4*x_1**2
ty_2 = 4*x*x_2+y_2-4*x_2**2


# Plot all lines
plt.plot(x,y)
plt.plot(x,ty_1)
plt.plot(x,ty_2)
# plt.plot(x,ty)
plt.plot(x_0,y_0,'o')
plt.text(x_0+.1,y_0,r"$P(x_0,y_0)$")
plt.plot(x_1,y_1,'og')
plt.plot(x_2,y_2,'og')

plt.show()
