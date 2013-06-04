A=[0 1;
   0 0];


F=(eye(size(A)+A)*x+B*u;


%% Kalman Filter
%% Prediction Step
xhat=F*x+B*u; % Predicted state estimate
Phat=F*P*F'+Q; % Predicted estimate covariance
%% Observation Step
y=z-H*xhat; % Innovation: Measurement residual
S=H*Phat*H'+R; % Innovation: Residual Covariance
%% Update Step
K=Phat*H'*inv(S) % Kalman gain
x=xhat+K*y; % Updated state estimate
P=(eye(size(A))-K*H)*Phat
