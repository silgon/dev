from rlpy.Tools import plt, mpatches, fromAtoB
from rlpy.Domains.Domain import Domain
import numpy as np

class GridMDPTut(Domain):
    """
    Simple Grid
    """
    #: Reward for each timestep spent in the goal region
    GOAL_REWARD = 1
    #: Reward for each timestep
    # STEP_REWARD = -.01
    STEP_REWARD = 0
    #: possible actions
    ACTIONS = np.array([[-1, 0], [+1, 0], [0, -1], [0, +1]])

    def __init__(self, gridSize=(2, 2)):
        """
        :param gridSize: Number of states \'n\' in the chain.
        """
        self.gridSize          = gridSize
        # self.start              = np.array([0,0])
        self.goal               = np.array([gridSize - 1, gridSize - 1])
        self.statespace_limits  = np.array([[0, gridSize-1], [0, gridSize-1]])
        self.episodeCap         = gridSize**2
        # self.continuous_dims    = []
        self.DimNames           = ['x', 'y']
        self.actions_num        = self.ACTIONS.shape[0]
        self.discount_factor    = 0.9
        super(GridMDPTut, self).__init__()

    def step(self, a):
        s = self.state.copy()
        ns = s+self.ACTIONS[a]
        ns = np.where(ns < 0, 0, ns)
        gridSize = self.gridSize
        ns = np.where(ns > gridSize-1, gridSize-1, ns)

        self.state = np.array(ns)

        terminal = self.isTerminal()
        r = self.GOAL_REWARD if terminal else self.STEP_REWARD
        return r, ns, terminal, self.possibleActions()

    def s0(self):
        self.state = np.array([0, 0])
        return self.state, self.isTerminal(), self.possibleActions()

    def isTerminal(self):
        s = self.state
        return np.array_equal(s, self.goal)

    def possibleActions(self, s=None):
        possibleA = np.array([], np.uint8)
        for a in xrange(self.actions_num):
            possibleA = np.append(possibleA, [a])
        return possibleA
