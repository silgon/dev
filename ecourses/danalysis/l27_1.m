clear all; close all; clc;

n=5000;
t=linspace(0,1/8,n);
f=sin(1394*pi*t)+sin(3266*pi*t);
ft=dct(f);
 
% subplot(2,1,1), plot(t,f)
% subplot(2,1,2), plot(ft)

% read signal
% Note: nyquist sample at twice the frequency of the signal
m=500;
r1=randintrlv([1:n],723);
perm=r1(1:m);
f2=f(perm);
t2=t(perm);

D=dct(eye(n,n));
A=D(perm,:);

x=pinv(A)*f2';
x2=A\f2';
cvx_begin;
variable x3(n);
minimize( norm(x3,1) );
subject to
A*x3 == f2';
cvx_end;

plot(t,f,'k',t2,f2,'mo')