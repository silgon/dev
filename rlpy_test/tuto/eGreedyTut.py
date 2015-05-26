from rlpy.Policies.Policy import Policy
import numpy as np

class eGreedyTut(Policy):
    """
    From the tutorial in policy creation.  Identical to eGreedy.py.
    """
 
    # Probability of selecting a random action instead of greedy
    epsilon         = None
    # Temporarily stores value of ``epsilon`` when exploration disabled
    old_epsilon     = None
    # bool, used to avoid random selection among actions with the same values
    forcedDeterministicAmongBestActions = None
    def __init__(self,representation, epsilon = .1,
                 forcedDeterministicAmongBestActions = False, seed=1):
        self.epsilon = epsilon
        self.forcedDeterministicAmongBestActions = forcedDeterministicAmongBestActions
        super(eGreedyTut,self).__init__(representation)
    def pi(self,s, terminal, p_actions):
        coin = self.random_state.rand()
        #print "coin=",coin
        if coin < self.epsilon:
            return self.random_state.choice(p_actions)
        else:
            b_actions = self.representation.bestActions(s, terminal, p_actions)
            if self.forcedDeterministicAmongBestActions:
                return b_actions[0]
            else:
                return self.random_state.choice(b_actions)
    def turnOffExploration(self):
        self.old_epsilon = self.epsilon
        self.epsilon = 0
    def turnOnExploration(self):
        self.epsilon = self.old_epsilon
