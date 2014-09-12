#! /bin/python
import numpy as np

# values for map:
# S: starting point
# P: Punishment
# G: Goal
alpha = 0.8
gamma = 0.2
# making map
grid = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'P', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
# making grid with python array
tmp = [[{' ': 0, 'S': 0, 'G': 1, 'P': -1, }[t] for t in x] for x in grid]
# making grid with numpy
pam = np.array(tmp)

# getting starting position
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = s = [i, j]


# check if it's the goal position
def isGoal(grid, s):
    """
    is the goal position
    Arguments:
    - `grid`: grid
    - `s`: state
    """
    return grid[s[0]][s[1]] == 'G'


class L():
    """Learning
    """
    def __init__(self, x, y, z):
        """
        Arguments:
        - `x`:
        - `y`:
        - `z`:
        """
        self._x = x
        self._y = y
        self._z = z
        self._Q = np.zeros((x, y, z))
        self._V = np.zeros((x, y))

    def getQVal(self, s, a):
        """get Q value given state and action
        Arguments:
        - `s`:
        - `a`:
        """
        x, y = s
        z = a
        return self._Q[x, y, z]

    def setQVal(self, s, a, val):
        """get Q value given state and action
        Arguments:
        - `s`:
        - `a`:
        """
        x, y = s
        z = a
        self._Q[x, y, z] = val

    def nextState(self, s, a):
        """ next current value taking into account some option
        Arguments:
        - `s`: state
        - `a`: action
        """
        nxt = {
            0: [s[0]+1, s[1]],  # up
            1: [s[0]-1, s[1]],  # down
            2: [s[0], s[1]-1],  # left
            3: [s[0], s[1]+1],  # right
            4: [s[0], s[1]],  # nothing
        }[a]
        nxt[0] = self._x-1 if nxt[0] == -1 else 0 if nxt[0] == self._x else nxt[0]
        nxt[1] = self._y-1 if nxt[1] == -1 else 0 if nxt[1] == self._y else nxt[1]
        return nxt
# Creating the values
x, y = pam.shape
z = 5  # 4 possible agent movements
Q = L(x, y, z)
R = 0

# Learning
for iters in range(1000):
    s = start
    # while we're not at the goal position
    while True:
        a = np.random.permutation(5)[0]  # policy: random permutation
        s_p = Q.nextState(s, a)
        a_p = np.random.permutation(5)[0]  # policy: random permutation
        Q_k = Q.getQVal(s, a)
        Q_k1 = Q.getQVal(s_p, a_p)
        R = pam[s[0], s[1]]
        tmp = Q_k+alpha*(R+gamma*Q_k1-Q_k)
        Q.setQVal(s, a, tmp)
        if isGoal(grid, s):
            break
        s = s_p

np.set_printoptions(precision=5)
np.set_printoptions(suppress=True)
print(Q._Q.max(2))
# print(Q._Q.min(2))
