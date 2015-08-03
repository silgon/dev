import numpy as np

def featureExpectations(P, pi, discount=0.9):
    """
    Feature Expectations based on States and policy (pi)

    Parameters
    ==========
    P: np.array of size SxSx3
        Transition matrix
    pi: np.array of size S
        best policy for every state
    discount: float
        discount factor

    Returns
    ======
    exp_normalized: np.array of size S
        feature expectations given the policy pi
    """
    S = P.shape[0]
    # x = dot(inv(A),y)
    A = np.zeros((S, S))
    A += np.diag(np.ones(S))
    # it was working just fine with next line but t was bigger
    # A = np.ones((S, S))
    for s in xrange(S):
        a = pi[s]
        for sp in xrange(S):
            if P[s, sp, a] == 0:
                continue
            A[sp, s] = A[sp, s] - discount*P[s, sp, a]
    # next step performs apparently better than original (next commented line)
    # return np.dot(np.linalg.inv(A), np.ones((S, 1))/S).ravel()
    expectation = np.dot(np.linalg.inv(A), np.ones((S, 1))).ravel()
    exp_normalized = expectation/np.sum(expectation)
    return exp_normalized


def featureExpectations2(P, pi, N_Demos=100, max_steps=40,discount=0.9):
    """
    Feature Expectations based on States and policy (pi)
    (Another computation method)

    Parameters
    ==========
    P: np.array of size SxSx3
        Transition matrix
    pi: np.array of size S
        best policy for every state
    discount: float
        discount factor

    Returns
    ======
    exp_normalized: np.array of size S
        feature expectations given the policy pi
    """
    S = P.shape[0]
    start = np.random.randint(0, S, N_Demos)
    demos_s = []
    demos_a = []
    for s in start:
        ss = []
        aa = []
        iters = 0
        for _ in xrange(max_steps):
            ss.append(s)
            aa.append(pi[s])
            s = np.argmax(P[s, :, pi[s]])
            iters += 1
            # we could add an if something to beak the loop
            # like repeated states
        demos_s.append(ss)
        demos_a.append(aa)
    mu_k = np.zeros(S)
    for i in xrange(N_Demos):
        for t in xrange(len(demos_s[i])):
            mu_k[demos_s[i][t]] = mu_k[demos_s[i][t]] + discount**t
    mu_k = mu_k/N_Demos
    return mu_k
