#! /usr/bin/python
"""
Simple example for IRL based on apprenticeship learning
"""
from __future__ import print_function
import numpy as np

from domain import *
from mdp import valueIteration
from feature_expectations import *
from irl import IRL

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
    demos = createRandomDemos(N_Demos, P, R, pi)
    # print(demos)
    irl = IRL(P, demos, 0.9)
    # print(irl)
