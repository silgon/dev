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
    Phat = (self.A * self.P) * np.transpose(self.A) + self.Q # covariance estimate
    #--------------------------Observation step-----------------------------
    ytil = z - self.H*xhat # innovation: measurement residual
    S = self.H*Phat*np.transpose(self.H) + self.R # innovation: residual covariance 
    #-----------------------------Update step-------------------------------
    K = Phat * np.transpose(self.H) * np.linalg.inv(S) # kalman gain
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

numsteps = 60

A = np.matrix([1])
H = np.matrix([1])
B = np.matrix([0])
Q = np.matrix([0.00001])
R = np.matrix([0.1])
xhat = np.matrix([3])
P    = np.matrix([1])

filter = KalmanFilterLinear(A,B,H,xhat,P,Q,R)
voltmeter = Voltmeter(1.25,0.25)

measuredvoltage = []
truevoltage = []
kalman = []

for i in range(numsteps):
    measured = voltmeter.GetVoltageWithNoise()
    measuredvoltage.append(measured)
    truevoltage.append(voltmeter.GetVoltage())
    kalman.append(filter.GetCurrentState()[0,0])
    filter.Step(np.matrix([0]),np.matrix([measured]))

pylab.plot(range(numsteps),measuredvoltage,'b',range(numsteps),truevoltage,'r',range(numsteps),kalman,'g')
pylab.xlabel('Time')
pylab.ylabel('Voltage')
pylab.title('Voltage Measurement with Kalman Filter')
pylab.legend(('measured','true voltage','kalman'))
pylab.show()
