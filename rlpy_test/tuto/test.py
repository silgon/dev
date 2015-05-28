#!/usr/bin/env python
"""
Agent Tutorial for RLPy
=================================

Assumes you have created the SARSA0.py agent according to the tutorial and
placed it in the current working directory.
Tests the agent on the GridWorld domain.
"""
__author__ = "Robert H. Klein"
from rlpy.Domains import GridWorld
from rlpy.Representations import Tabular, RBF
from rlpy.Policies import eGreedy
from rlpy.Experiments import Experiment
from rlpy.Agents import SARSA
from rlpy.Agents import Q_Learning
import os

from SARSA0 import SARSA0
from IncrTabularTut import IncrTabularTut
from ChainMDPTut import ChainMDPTut
from eGreedyTut import eGreedyTut
from GridMDPTut import GridMDPTut

def make_experiment(exp_id=1, path="./Results/Tutorial/gridworld-sarsa0"):
    """
    Each file specifying an experimental setup should contain a
    make_experiment function which returns an instance of the Experiment
    class with everything set up.

    @param id: number used to seed the random number generators
    @param path: output directory where logs and results are stored
    """

    opt = {}
    opt["exp_id"] = exp_id
    opt["path"] = path

    ## Domain:
    # maze = '4x5.txt'
    # domain = GridWorld(maze, noise=0.3)

    # chainSize = 20
    # domain = ChainMDPTut(chainSize=chainSize)

    gridSize = 5
    domain = GridMDPTut(gridSize=gridSize)

    opt["domain"] = domain

    ## Representation
    # discretization only needed for continuous state spaces, discarded otherwise
    # representation  = Tabular(domain, discretization=20)
    representation  = IncrTabularTut(domain)
    # resolution=25.
    # num_rbfs=1000.
    # representation = RBF(domain, num_rbfs=int(num_rbfs),
    #                      resolution_max=resolution, resolution_min=resolution,
    #                      const_feature=False, normalize=True, seed=exp_id)
    ## Policy
    # policy = eGreedy(representation, epsilon=0.2)
    policy = eGreedyTut(representation, epsilon=0.2)

    ## Agent
    # opt["agent"] = SARSA0(representation=representation, policy=policy,
    #                discount_factor=domain.discount_factor,
    #                    initial_learn_rate=0.1)
    # opt["agent"] = SARSA(representation=representation, policy=policy,
    #                      discount_factor=domain.discount_factor,
    #                      initial_learn_rate=0.1)
    opt["agent"] = Q_Learning(representation=representation, policy=policy,
                       discount_factor=domain.discount_factor,
                       initial_learn_rate=0.1,
                       learn_rate_decay_mode="boyan", boyan_N0=100,
                       lambda_=0.)


    opt["checks_per_policy"] = 10
    opt["max_steps"] = 1000
    opt["num_policy_checks"] = 10
    experiment = Experiment(**opt)
    return experiment

if __name__ == '__main__':
    experiment = make_experiment(1)
    experiment.run(visualize_steps=False,  # should each learning step be shown?
                   visualize_learning=True,  # show policy / value function?
                   visualize_performance=1)  # show performance runs?
    experiment.plot()
    experiment.save()
