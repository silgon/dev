from __future__ import print_function
import numpy as np
from mdp import valueIteration
from feature_expectations import *

def IRL(P, demos, discount=0.9):
    """
    Apprenticeship Learning

    Parameters
    ==========
    P: np.array of size SxSx3
        Transition matrix
    demos: list of lists [[[state, action],...],...]
        all state-actions that the agent performed
    discount: float
        discount factor

    Returns
    ======
    r: np.array of size S
        Reward of every state
    V: np.array of size S
        Expected values of the states
    pi: np.array of size S
        best policy for every state
    """
    # \mu_E construction
    S = P.shape[0]
    N = len(demos)
    muE = np.zeros(S)
    for i in xrange(N):
        for t in xrange(len(demos[i])):
            muE[demos[i][t][0]] = muE[demos[i][t][0]] + discount**t
    muE = muE/N
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
    epsilon = 0.0001
    # quit while loop if difference in t is little
    while abs(t-told) >= epsilon:
        told = t
        # compute expectations under last policy
        expectations = featureExpectations2(P, solutions[itr][1])
        mu = expectations  # features are the states
        # append mus
        mus.append(mu)
        if itr == 0:
            mu_bar = mu
        else:
            mu_bar_prev = mu_bars[itr-1]
            num = np.sum((mu-mu_bar_prev)*(muE-mu_bar_prev))
            den = np.sum((mu-mu_bar_prev)*(mu-mu_bar_prev))
            ratio = num/den
            mu_bar = mu_bar_prev + ratio*(mu-mu_bar)
        # compute weights and t
        mu_bars.append(mu_bar)
        w = muE - mu_bar
        t = np.linalg.norm(w)
        # Recompute optimal policy using new weights.
        soln = valueIteration(P, w)
        # add to list of weights and solutions
        weights.append(w)
        solutions.append(soln)
        itr += 1  # number of mus until now
        print("IRL iteration with t=", t)

    # compute last policy
    expectations = featureExpectations2(P, solutions[itr][1])
    itr += 1  # consistency with number of mus
    mu = expectations  # features are the states
    mus.append(mu)

    # create mu_mat matrix for optimization step
    mu_mat = np.zeros((S, itr))
    for i in xrange(itr):
        mu_mat[:, i] = mus[i]

    import cvxpy as cvx
    # Construct optimization problem.
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

    # create weights based on lambdas and mu_mat matrix
    w = np.dot(np.atleast_2d(lambd.value).T, mu_mat.T)
    w = np.ravel(w)  # for some reason w.ravel() is not working
    # because features and same as states
    r = w
    V, pi, Q = valueIteration(P, w)
    return dict(r=r, V=V, pi=pi, Q=Q)
