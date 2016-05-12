# p_size = 5
# p = [1./p_size for i in range(p)]
p = [0.2, 0.2, 0.2, 0.2, 0.2]
# p = [0., 0., 1., 0., 0.]
world = ["green", "red", "red", "green", "green"]

measurements = ["green", "red", "red"]
motions = [1, 1, 1]

pHIT = 0.6
pMISS = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    """
    p: probabilities
    Z: observation
    """
    q=[]
    for i in xrange(len(p)):
        hit = (Z==world[i])
        q.append(p[i]*(hit*pHIT+(1-hit)*pMISS))
    s = sum(q)
    for i in xrange(len(q)):
        q[i] = q[i]/s
    return q

# for m in measurements:
#     p = sense(p, m)
# print p

def move(p, U):
    """
    p: probabilities
    U: action
    """
    q = []
    for i in xrange(len(p)):
        s = pExact*p[(i-U)%len(p)]
        s = s + pOvershoot*p[(i-U-1)%len(p)]
        s = s + pUndershoot*p[(i-U+1)%len(p)]
        q.append(s)
        # q.append(p[(i-U)%len(p)])  # pExact=1
    return q

for i in xrange(len(motions)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])
    print p
