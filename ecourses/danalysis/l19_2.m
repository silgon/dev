% for more documentation in this program, check out file l19_1, this
% program is only meant to prove that it doesn't matter if you transpose
% your data

clear all; close all; clc;
% space and time
x=linspace(-10,10,100);
t=linspace(0,10,30);
[X,T]=meshgrid(x,t);

f=sech(X).*(1-0.5*cos(2*T))+(sech(X).*tanh(X)).*(1-0.5*sin(2*T));

subplot(2,2,1), 
waterfall(X,T,f),colormap([0 0 0])

[u,s,v]=svd(f');

for j=1:3
   ff=u(:,1:j)*s(1:j,1:j)*v(:,1:j)'; 
   % plot
   subplot(2,2,j+1)
   waterfall(X,T,ff'),colormap([0 0 0])
end
