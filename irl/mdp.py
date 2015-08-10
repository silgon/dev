import numpy as np

def valueIteration(P, R, discount=0.9, max_iter=1000):
    """
    Solves the Policy Iteration given the transition matrix and Rewards

    Parameters
    ==========
    P: np.array of size SxSx3
        Transition matrix
    R: np.array of size S
        Reward matrix
    discount: float
        discount factor
    max_iter: int
        maximum number of iterations

    Returns
    =======
    V: np.array of size S
        Expected values of the states
    pi: np.array of size S
        best policy for every state
    Q: np.array of size SxA
        Q values
    """
    S = P.shape[0]
    A = P.shape[2]
    Q = np.zeros((S, A))
    V = np.zeros(S)
    epsilon = 0.001
    iters = 0
    while True:
        delta = 0
        for i in xrange(S):
            tmp = V[i]
            # max
            for j in xrange(A):
                # sum_{s'} p(s'|s,a)[r(s,a,s')+\discount v(s')]
                Q[i, j] = np.sum([P[i, k, j]*(R[k] + discount*V[k])
                                  if not P[i, k, j] == 0 else 0
                                  for k in xrange(S)])
                # Q[i, j] = np.sum([P[i, k, j]*(R[k] + discount*V[k])
                #                   for k in xrange(S)])
            # max of Q is V
            V[i] = np.max(Q[i, :])
            delta = max(delta, abs(tmp-V[i]))

        # if delta is small or we reach max_iter exit while loop
        iters += 1
        if delta < epsilon or iters == max_iter:
            break
    # get policy from Q
    pi = np.argmax(Q, 1)
    return V, pi, Q
