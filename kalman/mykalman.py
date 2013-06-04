# kalman1.py
# written by Greg Czerniak (email is greg {aT] czerniak [dOt} info )
#
# Implements a single-variable linear Kalman filter.
#
# Note: This code is part of a larger tutorial "Kalman Filters for Undergrads"
# located at http://greg.czerniak.info/node/5.
import random
import numpy as np
import matplotlib.pyplot as plt

# Implements a linear Kalman filter.
class KalmanFilterLinear:
  def __init__(self,_A, _B, _H, _x, _P, _Q, _R):
    self.A = np.eye(_A.shape[0])+_A                      # State transition matrix.
    self.B = _B                      # Control matrix.
    self.H = _H                      # Observation matrix.
    self.x = _x                      # Initial state estimate.
    self.P = _P                      # Initial covariance estimate.
    self.Q = _Q                      # Estimated error in process.
    self.R = _R                      # Estimated error in measurements.
  def GetCurrentState(self):
    return self.x
  def Step(self,u,z): # u:control vector, z: measurement
    #---------------------------Prediction step-----------------------------
    xhat = self.A * self.x + self.B * u # predicted state
    Phat = (self.A * self.P) * self.A.T + self.H*self.Q*self.H.T # covariance estimate
    #--------------------------Observation step-----------------------------
    ytil = z - self.H*xhat # innovation: measurement residual
    S = self.H*Phat*self.H.T + self.R # innovation: residual covariance 
    #-----------------------------Update step-------------------------------
    K = Phat * self.H.T * np.linalg.inv(S) # kalman gain
    self.x = xhat + K * ytil
    # We need the size of the matrix so we can make an identity matrix.
    size = self.P.shape[0]
    self.P = (np.eye(size)-K*self.H)*Phat

class System1():
  """ This is a really easy system
  """
  
  def __init__(self, _A,_B,_Q):
    """
    
    Arguments:
    - `_A`:
    - `_B`:
    """
    self.A = np.eye(_A.shape[0])+_A                      # State transition matrix.
    self.B = _B
    self.Q=_Q
  def getVal(self,x,u):
    return self.A*x+self.B*u
  def getNVal(self,x,u):
    return self.getVal(x,u)+np.multiply(self.Q,np.random.randn(self.Q.shape[0],self.Q.shape[1]))*np.mat(np.ones((self.Q.shape[1],1)))

numsteps = 50

A=np.mat('0 1; 0 0')
B=np.mat('0 0; 0 1')
R=np.mat('0.1 0.1; 0.1 0.1')
H = np.mat('1 0; 0 1') # observation matrix
Q = np.mat('1 1; 1 1') # error in process
R = np.mat('1.5 1.5; 1.5 1.5') # error in measurements
xhat = np.mat('2;0') # first estimated value
x = np.mat('1;1') # first value
P= np.mat('.1 .1; .1 .1') # first estimated covariance estimate

filter = KalmanFilterLinear(A,B,H,xhat,P,Q,R)
s1=System1(A,B,Q)
measures = xhat
real = x
kalman = filter.GetCurrentState()

for i in range(numsteps):
  u=np.mat([[0],[1]])
  measured = s1.getNVal(x,u)
  measures=np.hstack((measures,measured))
  # x=measured
  real=np.hstack((real,s1.getVal(x,u)))
  x=s1.getVal(x,u)
  # real.append(voltmeter.GetVoltage())
  # print filter.GetCurrentState()
  kalman=np.hstack((kalman,filter.GetCurrentState()))
  filter.Step(u,measured)
measures=measures.T
real=real.T
kalman=kalman.T
plt.plot(measures[:,0],measures[:,1],'g+',
         kalman[:,0],kalman[:,1],'r',
         real[:,0],real[:,1],'b',
         )
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('')
# plt.legend(('measured','true voltage','kalman'))
plt.show()
