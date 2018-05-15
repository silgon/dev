# reference: https://srcole.github.io/2015/06/14/guess/
import numpy as np
# Functions to calculate optimal trading strategies for each player
def nWin(n1,n_other,N):
    '''
    Calculate # of numbers controlled by the player who guessed 'n1'
    in a game of range 'N' in which the other guesses are in the
    array 'n_other'
    '''
    # Game is invalid if any players choose the same number
    if n1 in n_other:
        return 0
        
    nowin = []
    for no in range(len(n_other)):
        nowin = np.hstack((nowin,numCloser(n_other[no],n1,N)))
    return N - len(np.unique(nowin))


def numCloser(n1,n2,N):
    '''
    Calculate the numbers that are closer to 'n1' compared to 'n2'
    in the entire range [0,N]
    '''
    x1 = np.abs(np.arange(N) - n1)
    x2 = np.abs(np.arange(N) - n2)
    All = np.arange(N)
    return All[x1<=x2]


def closest(nps,N):
    '''
    Calculate the players (whose bets are in 'nps') that are closest
    to each number in the range [0,N]
    '''
    P = len(nps)
    closescore = np.zeros([P,N])
    for p in range(P):
        closescore[p,:] = np.abs(np.arange(N) - nps[p])
    
    closests = np.argmin(closescore,axis=0)
    for n in range(N):
        temp1 = np.min(closescore[:,n])
        if sum(closescore[:,n] == temp1) != 1:
            closests[n] = -1
    
    return closests

# Experiment parameters
P = 2 #Number of players
N = 20 #Range of integers in the game

# Calculate the number of numbers controlled by each player for each possible combination of choices
W = np.zeros([N,N,P],dtype=np.int)
for n1 in range(N):
    for n2 in range(N):
        W[n1,n2,0] = nWin(n1,[n2],N)
        W[n1,n2,1] = nWin(n2,[n1],N)

# Calculate the optimal number choices for P1 and P2
p1_bestres_eachn = np.zeros(N)
for n in range(N):
    p1_bestres_eachn[n] = N - np.max(np.squeeze(W[n,:,1]))
p1bestN = np.argmax(p1_bestres_eachn)
p2bestN = np.argmax(np.squeeze(W[p1bestN,:,1]))
p2bestW = W[p1bestN,p2bestN,1]
p1bestW = W[p1bestN,p2bestN,0]

# Display results of strategically played game
print 'P1 chooses' , p1bestN , '... Controls' , np.int(p1bestW), '/', N, 'numbers'
print 'P2 chooses' , p2bestN , '... Controls' , np.int(p2bestW), '/', N, 'numbers'

# Experiment parameters
P = 3 #Number of players
N = 50 #Range of integers in the game

# Calculate the number of numbers controlled by each player for each possible combination of choices
W = np.zeros([N,N,N,P],dtype=np.int)
for n1 in range(N):
    for n2 in range(N):
        for n3 in range(N):
            W[n1,n2,n3,0] = nWin(n1,[n2,n3],N)
            W[n1,n2,n3,1] = nWin(n2,[n1,n3],N)
            W[n1,n2,n3,2] = nWin(n3,[n1,n2],N)

# Calculate the best choices for P2 and P3 for every possible choice by P1
p2bestN_1 = np.zeros(N,dtype=np.int)
p3bestN_1 = np.zeros(N,dtype=np.int)
p1bestW = np.zeros(N)
p2bestW = np.zeros(N)
p3bestW = np.zeros(N)
for n1 in range(N):
    # Calculate the best possible P2W for every n2
    p2_bestres_eachn = np.zeros(N)
    for n2 in range(N):
        c_bestp3 = np.argmax(np.squeeze(W[n1,n2,:,2]))
        p2_bestres_eachn[n2] = W[n1,n2,c_bestp3,1]
        
    # Choose best P2N, followed by P3N
    p2bestN_1[n1] = np.argmax(p2_bestres_eachn)
    p3bestN_1[n1] = np.argmax(np.squeeze(W[n1,p2bestN_1[n1],:,2]))
    
    # Calculate winnings for all players
    p1bestW[n1] = W[n1,p2bestN_1[n1],p3bestN_1[n1],0]
    p2bestW[n1] = W[n1,p2bestN_1[n1],p3bestN_1[n1],1]
    p3bestW[n1] = W[n1,p2bestN_1[n1],p3bestN_1[n1],2]

# Calculate the best option for P1 and its instantiations
p1bestN = np.argmax(p1bestW)
p2bestN = p2bestN_1[p1bestN]
p3bestN = p3bestN_1[p1bestN]
p1bestW = W[p1bestN,p2bestN,p3bestN,0]
p2bestW = W[p1bestN,p2bestN,p3bestN,1]
p3bestW = W[p1bestN,p2bestN,p3bestN,2]


# Display optimal game
print 'P1 chooses' , p1bestN , '... Controls' , np.int(p1bestW), '/', N, 'numbers'
print 'P2 chooses' , p2bestN , '... Controls' , np.int(p2bestW), '/', N, 'numbers'
print 'P3 chooses' , p3bestN , '... Controls' , np.int(p3bestW), '/', N, 'numbers'
