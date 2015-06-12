#! /usr/bin/python
"""
Simple example for IRL based on apprenticeship learning
"""
from __future__ import print_function
import numpy as np


def linearMDP(S=5, goal=3):
    """
    Chain MDP with 3 actions, [-1, 0, +1]

    Parameters
    =========
    S: int
        Size of the chain
    goal: int
        where the reward is 1, for all the rest reward is zero

    Returns
    =======
    P: np.array of size SxSx3
        Transition matrix
    R: np.array of size S
        Reward matrix
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

    Parameters
    ==========
    P: np.array of size SxSx3
        Transition matrix
    R: np.array of size S
        Reward matrix
    gamma: float
        discount factor
    max_iter: int
        maximum number of iterations

    Returns
    =======
    V: np.array of size S
        Expected values of the states
    pi: np.array of size S
        best policy for every state
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
                                  if not P[i, k, j] == 0 else 0
                                  for k in xrange(S)])
                # Q[i, j] = np.sum([P[i, k, j]*(R[k] + gamma*V[k])
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
    return V, pi


def createRandomDemos(N_Demos, P, R, pi):
    """
    Create demonstrations to use with the IRL algorithm

    Parameters
    ==========
    N_Demos: int
        number of demonstrations you want for the IRL
    P: np.array of size SxSx3
        Transition matrix
    R: np.array of size S
        Reward matrix
    pi: np.array of size S
        best policy for every state

    Returns
    ======
    demos_s: list of lists
        all the states in which the agent was
    demos_a: list of lists
        all actions that the agent performed
    """
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


def IRL(P, demos_s, demos_a, discount=0.9):
    """
    Apprenticeship Learning

    Parameters
    ==========
    P: np.array of size SxSx3
        Transition matrix
    demos_s: list of lists
        all the states in which the agent was
    demos_a: list of lists
        all actions that the agent performed
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
    N = len(demos_s)
    muE = np.zeros(S)
    for i in xrange(N):
        for t in xrange(len(demos_s[i])):
            muE[demos_s[i][t]] = muE[demos_s[i][t]] + discount**t
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
    V, pi = valueIteration(P, w)
    return dict(r=r, V=V, pi=pi)



if __name__ == '__main__':
    """ Main Program """
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
