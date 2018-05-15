import numpy as np

def win(p1, p_arr):
    if p1 in p_arr:
        return 0 # this case should never enter
    c = p_arr<p1 # condition
    left = p_arr[c]
    right = p_arr[~c]
    p_l = 0
    p_r = 1
    if len(left)>0:
        t_ = np.max(left)
        p_l =(t_+p1)/2
    if len(right)>0:
        t_ = np.min(right)
        p_r =(t_+p1)/2
    return p_r-p_l

x = np.array([.1,.7,.9])
res = [win(x[i],np.delete(x,i)) for i in range(len(x))]

import matplotlib.pyplot as plt
P = 2
N = 50
tmp = np.linspace(0,1,N)
# X, Y = np.meshgrid(tmp, tmp)
# Z = np.zeros_like(X)
# for i in range(N):
#     for j in range(N):
#         Z[i,j] = win(X[i,j], np.array([Y[i,j]]))
# plt.pcolor(X, Y, Z)
# plt.colorbar()
# plt.show()
W = np.zeros([N, N, P])
for n1 in range(N):
    for n2 in range(N):
        W[n1,n2,0] = win(tmp[n1],np.array([tmp[n2]]))
        W[n1,n2,1] = win(tmp[n2],np.array([tmp[n1]]))

p2_am = np.argmax(W[:,:,1],axis=1)
p1_am = np.argmax([W[n1,p2_am[n1],0] for n1 in range(N)])
print(W[p1_am,p2_am[p1_am]])

