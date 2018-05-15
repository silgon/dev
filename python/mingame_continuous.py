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
