clear all; close all; clc;
% space and time
x=linspace(0,1,25);
t=linspace(0,2,50);
% mesh of this values
[T,X]=meshgrid(t,x);

% function
f=exp(-abs((X-0.5).*(T-1)))+sin(X.*T);
subplot(2,2,1)
surf(X,T,f)

% low rank aproximation
[u,s,v]=svd(f);
for j=1:3
   ff=u(:,1:j)*s(1:j,1:j)*v(:,1:j)'; 
   % plot
   subplot(2,2,j+1)
   surf(X,T,ff)
end

% most of the function is contained in the first 3 values.
figure(2), 
plot(diag(s),'ko') % semilogy(diag(s),'ko')

% principal functions
% this is really important because when we want to transform a function we
% will decide that it's decomposed in taylor, sines and cosines, etc. All
% this information will be contained here, in the functions gived by the
% svd.
figure(3),
plot(x,u(:,1),'k',x,u(:,2),'r',x,u(:,3),'g') % how modes change in space
% plot(t,v(:,1),'k',t,v(:,2),'r',t,v(:,3),'g') % how modes change in time
