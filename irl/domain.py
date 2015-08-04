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
    demos = []
    for s in start:
        ss = []  # chain of states
        aa = []  # chain of actions
        while True:
            ss.append(s)
            aa.append(pi[s])
            if R[s] == np.max(R):
                break
            s = np.argmax(P[s, :, pi[s]])
        demo = zip(ss, aa)
        demos.append(demo)
    return demos
