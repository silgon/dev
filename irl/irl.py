#! /usr/bin/python
from __future__ import print_function
import numpy as np


def linearMDP(S=5, goal=3):
    """
    Linear MDP with 3 actions, [-1, 0, +1]
    """
    # Probability Matrix
    P = np.zeros((S, S, 3))
    P[np.array(range(1, S)+[0]), :, 0] = np.diag(np.ones(S))
    P[:, :, 1] = np.diag(np.ones(S))
    P[np.array([S-1]+range(0, S-1)), :, 2] = np.diag(np.ones(S))
    R = np.zeros(S)
    # Reward
    R[goal] = 1
    return P, R


def valueIteration(P, R, gamma=0.9, max_iter=1000):
    """
    Solves the Policy Iteration given the transition matrix and Rewards
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
                # sum_{s'} p(s'|s,a)[r(s,a,s')+\gamma v(s')]
                Q[i, j] = np.sum([P[i, k, j]*(R[k] + gamma*V[k])
                                  for k in xrange(S)])
            # max of Q is V
            V[i] = np.max(Q[i, :])
            delta = max(delta, abs(tmp-V[i]))

        # if delta is small or we reach max_iter exit while loop
        iters += 1
        if delta < epsilon or iters == max_iter:
            break
    # get policy from Q
    pi = np.argmax(Q, 1)
    return V, pi


def createRandomDemos(N_Demos, P, R, pi):
    S = P.shape[0]
    start = np.random.randint(0, S, N_Demos)
    demos_s = []
    demos_a = []
    for s in start:
        ss = []
        aa = []
        while True:
            ss.append(s)
            aa.append(pi[s])
            if R[s] == np.max(R):
                break
            s = np.argmax(P[s, :, pi[s]])
        demos_s.append(ss)
        demos_a.append(aa)
    return demos_s, demos_a


def featureExpectations(P, pi, discount=0.9):
    """
    Feature Expectations based on States and policy (pi)
    """
    S = P.shape[0]
    A = P.shape[2]
    ## x = dot(inv(A),y)
    A = np.ones((S,S))
    for s in xrange(S):
        A[s, s] = A[s, s]+1;
        a = pi[s]
        for sp in xrange(S):
            A[sp, s] = A[sp, s] - discount*P[s, sp, a]
    return np.dot(np.linalg.inv(A), np.ones((S, 1))/S).ravel()


def IRL(P, demos_s, demos_a, discount=0.9):
    """
    Apprenticeship Learning
    """
    # State Expectations
    S = P.shape[0]
    N = len(demos_s)
    muE = np.zeros(S)
    for i in xrange(N):
        for t in xrange(len(demos_s[i])):
            muE[demos_s[i][t]] = muE[demos_s[i][t]] + discount**(t-1)
    muE = muE/N
    # TODO(silgon): convert to features
    # Tabular, IncTabular, Fourier, RBF
    # Random Policy
    r = np.random.rand(S)  # states / use features later
    soln = valueIteration(P, r)
    weights = [r]
    solutions = [soln]
    mus = []
    mu_bars = []
    itr = 0

    # Initialize t.
    t = 100.0
    told = 0.0

    while True:
        told = t
        # compute expectations under last policy
        expectations = featureExpectations(P, solutions[itr][1])
        # TODO(silgon): convert to features
        mu = expectations  # features are the states
        # append mus
        mus.append(mu)
        if itr == 0:
            mu_bars.append(mu)
            mu_bar = mu_bars[itr]
            w = muE - mu_bar
            t = np.linalg.norm(w)
        else:
            mu_bar_prev = mu_bars[itr-1]
            num = np.sum((mu-mu_bar_prev)*(muE-mu_bar_prev))
            den = np.sum((mu-mu_bar_prev)*(mu-mu_bar_prev))
            ratio = num/den
            mu_bar = mu_bar_prev + ratio*(mu-mu_bar)
            w = muE - mu_bar
            t = np.linalg.norm(muE - mu_bar)
            mu_bars.append(mu_bar)
        # Recompute optimal policy using new weights.
        # remap features
        soln = valueIteration(P, w)
        weights.append(w)
        solutions.append(soln)
        itr += 1  # number of mus until now
        # quit while loop if difference in t is little
        print("IRL iteration with t=", t)
        if abs(t-told) <= 0.0001:
            break
    # compute last policy
    expectations = featureExpectations(P, solutions[itr][1])
    itr += 1  # consistency with number of mus
    # TODO(silgon): convert to features
    mu = expectations  # features are the states
    mus.append(mu)
    # for i in xrange(len(solutions)):
    #     print(solutions[i][1])
    mu_mat = np.zeros((S, itr))
    for i in xrange(itr):
        mu_mat[:, i] = mus[i]

    import cvxpy as cvx
    # Construct the problem.
    mu = cvx.Variable(S)
    lambd = cvx.Variable(itr)
    objective = cvx.Minimize(cvx.sum_squares(muE-mu))
    constraints = [mu == mu_mat*lambd,
                   lambd >= np.zeros(itr),
                   cvx.sum_entries(lambd) == 1]

    prob = cvx.Problem(objective, constraints)
    # The optimal objective is returned by prob.solve().
    # result = prob.solve(verbose=True)
    prob.solve(verbose=False)

    # create weights based on lambdas
    w = np.dot(np.atleast_2d(lambd.value).T, mu_mat.T)
    w = np.ravel(w)  # for some reason w.ravel() is not working
    # because features and same as states
    r = w
    V, pi = valueIteration(P, w)
    # print(solutions)
    return dict(r=r, V=V, pi=pi)



if __name__ == '__main__':
    np.random.seed(0)
    # Create MDP
    N_States = 40
    P, R = linearMDP(N_States, 2)
    # Solve MDP
    V, pi = valueIteration(P, R)
    # Create Examples state-actions pairs
    N_Demos = 10
    demos_s, demos_a = createRandomDemos(N_Demos, P, R, pi)
    # print(demos_s)
    # print(demos_a)
    irl = IRL(P, demos_s, demos_a, 0.9)
    # print(irl)
