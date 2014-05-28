clear all; close all; clc;

L=40; n=512;
x2=linspace(-L/2,L/2,n+1);
x=x2(1:n);
k=(2*pi/L)*[0:n/2-1 -n/2:-1]';

% time
t=0:0.5;10;
N=1;
u=N*sech(x);
ut=fft(u);

[t,utsol]=ode45('nls_example_rhs',t,ut,k);
for j=1:length(t)
   usol(j,:)=ifft(utsol(j,:)); 
end
waterfall(x,t,abs(usol)),colormap([0 0 0]);