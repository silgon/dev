clc; clf; clear all;
% values a and b in [x,y,theta]
a=[10 19 -pi/4];
b=[3 4 pi/4];

x1=a(1); y1=a(2); theta1=a(3);
x2=b(1); y2=b(2); theta2=b(3);

A=[x2-x1 y2-y1]';
B=[cos(theta1) -cos(theta2); sin(theta1) -sin(theta2)];

% calculating parameters for projection
s=inv(B)*A, % matrix method
z=(-(x2-x1)*sin(theta2)+(y2-y1)*cos(theta2))/sin(theta1-theta2) % by hand method

%% a,b
%% x1+s(1)*sin(theta1), y1+s(1)*cos(theta1)
hold on
plot(a(1),a(2),'r+')
plot(b(1),b(2),'r+')
plot(x1+s(1)*cos(theta1), y1+s(1)*sin(theta1),'r+')
plot(x1+z*cos(theta1), y1+z*sin(theta1),'ko') % same projection with by hand result
