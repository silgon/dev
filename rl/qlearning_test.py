#! /bin/python
import numpy as np

# values for map:
# S: starting point
# P: Punishment
# G: Goal

# making map
grid=[
[' ',' ',' ',' ',' ',' ',' ','G'],
[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ','P',' ',' ',' ',' ',' '],
[' ',' ','P',' ',' ',' ',' ',' '],
[' ',' ','P',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
['S',' ',' ',' ',' ',' ',' ',' ']
]
# making grid with python array
tmp=[[{' ': 0,'S': 0,'G': 1,'P': -1,}[t] for t in x] for x in grid] 
# making grid with numpy
pam = np.array(tmp)

# getting starting position
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]=='S': cur=[i,j]
# next current value taking into account some option
def nextCur(cur,op): 
    return {
        0: [cur[0]+1,cur[1]], # up
        1: [cur[0]-1,cur[1]], # down
        2: [cur[0],cur[1]-1], # left
        3: [cur[0],cur[1]+1], # right
    }[op]
x,y=pam.shape
z=4 # 4 possible agent movements
A=np.zeros((x,y,z))

#TODO, work with np.random.permutation(4)[0] to change the state


