clear all; close all; clc;

%% first part
T=30; % Domain
n=512; % points in the function

t2=linspace(-T/2,T/2,n+1);
t=t2(1:n); % we get rid of the last point because the last point is the same as the first
k=(2*pi/T)*[0:n/2-1 -n/2:-1]; % normalize to our domain (2*pi meaning frequency), and shifting because of the butterfly calculations happening in the fft
ks=fftshift(k); % shift the function for the fourier transformation

u=sech(t); % function
ut=fft(u); % fourier transform

% add noise
noise=20;
utn=ut+noise*(randn(1,n)+i*randn(1,n)); % fourier transform with white noise
un=ifft(utn);

filter=exp(-(k+0).^2); % filter
utnf=filter.*utn; % filtering the signal
unf=ifft(utnf); % inverse fft

% subplot(2,1,1), plot(t,u,'k',t,un,'m');
% subplot(2,1,2), plot(ks,abs(fftshift(ut))/max(abs(fftshift(ut))),'k',ks,abs(fftshift(utn))/max(abs(fftshift(utn))),'m');
subplot(2,1,1), plot(t,un,'m', t, unf,'g',t,0*t+.5,'k:');
axis([-15 15 0 1])
subplot(2,1,2), plot(ks,abs(fftshift(utn))/max(abs(fftshift(utn))),'m',...
    ks,abs(fftshift(filter))/max(abs(fftshift(filter))),'b',...
    ks,abs(fftshift(utnf))/max(abs(fftshift(utnf))),'g'...
    );

axis([-15 15 0 1])

