# kalman1.py
# written by Greg Czerniak (email is greg {aT] czerniak [dOt} info )
#
# Implements a single-variable linear Kalman filter.
#
# Note: This code is part of a larger tutorial "Kalman Filters for Undergrads"
# located at http://greg.czerniak.info/node/5.
import random
import numpy as np
import pylab

# Implements a linear Kalman filter.
class KalmanFilterLinear:
  def __init__(self,_A, _B, _H, _x, _P, _Q, _R):
    self.A = _A                      # State transition matrix.
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
    Phat = (self.A * self.P) * self.A.T + H*self.Q*H.T # covariance estimate
    #--------------------------Observation step-----------------------------
    ytil = z - self.H*xhat # innovation: measurement residual
    S = self.H*Phat*self.H.T + self.R # innovation: residual covariance 
    #-----------------------------Update step-------------------------------
    K = Phat * self.H.T * np.linalg.inv(S) # kalman gain
    self.x = xhat + K * ytil
    # We need the size of the matrix so we can make an identity matrix.
    size = self.P.shape[0]
    self.P = (np.eye(size)-K*self.H)*Phat

class Voltmeter:
  def __init__(self,_truevoltage,_noiselevel):
    self.truevoltage = _truevoltage
    self.noiselevel = _noiselevel
  def GetVoltage(self):
    return self.truevoltage
  def GetVoltageWithNoise(self):
    return random.gauss(self.GetVoltage(),self.noiselevel)
class System1():
  """
  """
  
  def __init__(self, _A,_B,_Q):
    """
    
    Arguments:
    - `_A`:
    - `_B`:
    """
    self.A = _A
    self.B = _B
    self.Q=_Q
  def getVal(self,x,u):
    return A*x+B*u
  def getNVal(self,x,u):
    return self.getVal(x,u)+np.multiply(Q,np.random.randn(Q.shape[0],Q.shape[1]))*np.mat(np.ones((Q.shape[1],1)))

numsteps = 50

# A = np.mat([2])
# H = np.mat([1]) # observation matrix
# B = np.mat([1]) # 
# Q = np.mat([0.00001]) # error in process
# R = np.mat([0.1]) # error in measurements
# xhat = np.mat([3]) # first estimated value
# P    = np.mat([1]) # first estimated covariance estimate

A=np.mat('0 1; 0 0')
B=np.mat('0 0; 0 1')
R=np.mat('0.1 0.1; 0.1 0.1')
H = np.mat('1 0; 0 1') # observation matrix
Q = np.mat('0.1 0.1; 0.1 0.1') # error in process
R = np.mat('0.1 0.1; 0.1 0.1') # error in measurements
xhat = np.mat('4;4') # first estimated value
x = np.mat('1;1') # first value

P    = np.mat('1 1; 1 1') # first estimated covariance estimate



filter = KalmanFilterLinear(A,B,H,xhat,P,Q,R)
# voltmeter = Voltmeter(1.25,0.25)
s1=System1(A,B,Q)
measuredvoltage = x
truevoltage = []
kalman = filter.GetCurrentState()

for i in range(numsteps):
  u=np.mat([[0],[float(i)**2/50]])
  measured = s1.getNVal(x,u)
  measuredvoltage=np.hstack((measuredvoltage,measured))
  x=measured
  # truevoltage.append(voltmeter.GetVoltage())
  # print filter.GetCurrentState()
  kalman=np.hstack((kalman,filter.GetCurrentState()))
  filter.Step(u,measured)

# pylab.plot(range(numsteps),measuredvoltage,'b',range(numsteps),truevoltage,'r',range(numsteps),kalman,'g')
pylab.plot(measuredvoltage[0,:],measuredvoltage[1,:],'b+',kalman[0,:],kalman[1,:],'r+')
pylab.xlabel('x1')
pylab.ylabel('x2')
pylab.title('tururu')
# pylab.legend(('measured','true voltage','kalman'))
pylab.show()
