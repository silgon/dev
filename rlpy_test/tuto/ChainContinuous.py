"""Puddle world domain (navigation task)."""

from rlpy.Domains.Domain import Domain
import numpy as np
import matplotlib.pyplot as plt

__copyright__ = "Copyright 2013, RLPy http://acl.mit.edu/RLPy"
__credits__ = ["Alborz Geramifard", "Robert H. Klein", "Christoph Dann",
               "William Dabney", "Jonathan P. How"]
__license__ = "BSD 3-Clause"
__author__ = "Omar Islas"


class ChainContinuous(Domain):

    """

    **STATE:** 2-dimensional vector, *s*, each dimension is continuous in [0,1]\n
    **ACTIONS:** [right, up, left, down] - NOTE it is not possible to loiter.\n
    **REWARD:** 0 for goal state, -1 for each step, and an additional penalty
        for passing near puddles.

    **REFERENCE:**

    .. seealso::
     Double integration approach
    .. seealso::
        Sutton, R. S.: Generalization in Reinforcement Learning:
        Successful Examples Using Sparse Coarse Coding, NIPS(1996)

    """

    discount_factor = 1.  # discout factor
    domain_fig = None
    valfun_fig = None
    polfun_fig = None

    episodeCap = 3000
    continuous_dims = np.arange(1)  # position
    statespace_limits = np.array([[-10., 10.]])
    actions_num = 3

    def __init__(self, noise_level=.01, discount_factor=1., dt=0.1):
        self.noise_level = noise_level
        self.discount_factor = discount_factor
        self.dt = dt
        super(ChainContinuous, self).__init__()

        # side_x = np.linspace(self.statespace_limits[0, 0],
        #                      self.statespace_limits[0, 1], 100)
        # side_y = np.linspace(self.statespace_limits[1, 0],
        #                      self.statespace_limits[1, 1], 100)
        # X, Y = np.meshgrid(side_x, side_y)
        # self.X, self.Y = X, Y
        # self.reward_map = np.zeros(self.X.shape)
        # self.val_map = np.zeros(self.X.shape)
        # self.pi_map = np.zeros(self.X.shape)

        # for i in xrange(X.shape[1]):
        #     for j in xrange(X.shape[0]):
        #         s = np.array([X[i, j], Y[i, j]])
        #         self.reward_map[i, j] = self._reward(s)

    def s0(self):
        mult = np.max(self.statespace_limits, 1) - np.min(self.statespace_limits, 1)
        self.state = self.random_state.rand()*mult-mult/2
        return self.state.copy(), self.isTerminal(), self.possibleActions()

    def isTerminal(self, s=None):
        if s is None:
            s = self.state[0]
        return 4.9 < s < 5.1

    def possibleActions(self, s=0):
        return np.arange(self.actions_num)

    def step(self, a):
        step_val = 0.05
        s = self.state[0]
        if a == 0:
            ns = s-step_val
        if a == 1:
            ns = s
        if a == 2:
            ns = s+step_val
        # make sure we stay inside the [0,1]^2 region
        ns = np.minimum(ns, self.statespace_limits[:, 1])
        ns = np.maximum(ns, self.statespace_limits[:, 0])
        self.state = ns.copy()
        return self._reward(ns), ns, self.isTerminal(), self.possibleActions()

    def _reward(self, s):
        if self.isTerminal(s):
            return 1  # goal state reached
        return 0

    # def showDomain(self, a=None):
    #     s = self.state
    #     # Draw the environment
    #     if self.domain_fig is None:
    #         self.domain_fig = plt.figure("Domain")
    #         self.reward_im = plt.imshow(self.reward_map, extent=(0, 1, 0, 1),
    #                                     origin="lower")
    #         self.state_mark = plt.plot(s[0], s[1], 'kd', markersize=20)
    #         plt.draw()
    #     else:
    #         self.domain_fig = plt.figure("Domain")
    #         self.state_mark[0].set_data([s[0]], [s[1]])
    #         plt.draw()

    # def showLearning(self, representation):
    #     X, Y = self.X, self.Y
    #     for i in xrange(X.shape[1]):
    #         for j in xrange(X.shape[0]):
    #             s = np.array([X[i, j], Y[i, j]])
    #             self.val_map[i, j] = \
    #                 representation.V(
    #                     s,
    #                     self.isTerminal(s),
    #                     self.possibleActions(s))
    #             self.pi_map[i, j] = \
    #                 representation.bestAction(
    #                     s,
    #                     self.isTerminal(s),
    #                     self.possibleActions())

    #     if self.valfun_fig is None:
    #         self.valfun_fig = plt.figure("Value Function")
    #         plt.clf()
    #         plt.pcolormesh(X, Y, self.val_map)
    #         plt.colorbar()
    #     else:
    #         self.valfun_fig = plt.figure("Value Function")
    #         plt.pcolormesh(X, Y, self.val_map)
    #     plt.draw()

    #     if self.polfun_fig is None:
    #         self.polfun_fig = plt.figure("Policy")
    #         plt.clf()
    #         plt.pcolormesh(X, Y, self.pi_map)
    #     else:
    #         self.polfun_fig = plt.figure("Policy")
    #         plt.pcolormesh(X, Y, self.pi_map)
    #     plt.draw()

    #     if self.domain_fig is None:
    #         self.polfun_fig = plt.figure("Reward")
    #         plt.clf()
    #         plt.pcolormesh(X, Y, self.reward_map)
    #         plt.colorbar()
    #     plt.draw()
