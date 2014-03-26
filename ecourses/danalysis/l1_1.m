clear all; close all; clc;
%% first part of the lecture
L=20; % Domain
n=128; % points in the function

x2=linspace(-L/2,L/2,n+1);
x=x2(1:n); % we get rid of the last point because the last point is the same as the first

k=(2*pi/L)*[0:n/2-1 -n/2:-1]; % normalize to our domain (2*pi meaning frequency), and shifting because of the butterfly calculations happening in the fft

u=exp(-x.^2); % my gaussian function

ut=fft(u); % fast fourier transform

plot(fftshift(k),abs(fftshift(ut))); % shifting the stuff


%% second part with a sech ecuation
L=20; % Domain. As in example for the gibbs phenomenon you can reduce de domain (like to 4). You'll see oscillations between the jump, since now the function is not periodic and we're violating that principle
n=128; % points in the function

x2=linspace(-L/2,L/2,n+1);
x=x2(1:n); % we get rid of the last point because the last point is the same as the first

k=(2*pi/L)*[0:n/2-1 -n/2:-1];

u=sech(x);
ud=-sech(x).*tanh(x);
u2d=sech(x)-2*sech(x).^3

ut=fft(u); % fast fourier transform

% check out the algorithm, spectral differentiation
uds=ifft((i*k).*ut); % inverse fourier transform 
u2ds=ifft((i*k).^2.*ut);
ks=fftshift(k);
plot(x,ud,'r',x,uds,'mo')
