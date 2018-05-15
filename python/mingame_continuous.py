import numpy as np

def win(p1, p_arr):
    """ get that p1 (float) gets given an array of points p_arr(numpy.array)
    """
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

# next code might be used later
# x = np.array([.1,.7,.9])
# res = [win(x[i],np.delete(x,i)) for i in range(len(x))]

P = 3 # number of points
N = 50 # number of samples (discretized problem)
tmp = np.linspace(0,1,N) # sample space

W = np.zeros([N, N, N, P])
for n1 in range(N):
    for n2 in range(N):
        for n3 in range(N):
            W[n1,n2,n3,0] = win(tmp[n1],tmp[[n2,n3]])
            W[n1,n2,n3,1] = win(tmp[n2],tmp[[n1,n3]])
            W[n1,n2,n3,2] = win(tmp[n3],tmp[[n1,n2]])

# find optimal values of P3 for all combinations of P2 and P1
p3_am = np.argmax(W[:,:,:,2],axis=2)
# find optimal values of P2 given max P3 for all combinations of P1
p2_am = np.argmax([[W[n1,n2,p3_am[n1,n2],1] for n2 in range(N)] for n1 in range(N)],axis=1)
# find optimal value of P1 max P2 given max P3
p1_am = np.argmax([W[n1,p2_am[n1],p3_am[n1,p2_am[n1]],0] for n1 in range(N)])
i1,i2,i3 = p1_am, p2_am[p1_am], p3_am[p1_am, p2_am[p1_am]]
positions = tmp[[i1,i2,i3]]
place = W[i1,i2,i3]

