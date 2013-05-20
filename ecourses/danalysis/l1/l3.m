clear all; close all; clc;

%% convergence of signal with a loop and white noise parameter
T=30; % Domain
n=512; % points in the function

t2=linspace(-T/2,T/2,n+1);
t=t2(1:n); % we get rid of the last point because the last point is the same as the first
k=(2*pi/T)*[0:n/2-1 -n/2:-1];
ks=fftshift(k); % shift the function for the fourier transformation

u=sech(t); % function
ut=fft(u); % fourier transform

% add noise
noise=30;
utn=ut+noise*(randn(1,n)+i*randn(1,n)); % fourier transform with white noise
un=ifft(utn);

avg=zeros(1,n);
realizations=30;
for j=1:realizations
    utn=ut+noise*(randn(1,n)+i*randn(1,n)); % fourier transform with white noise
    avg=avg+utn;
    avg2=abs(fftshift(avg))/j;
    plot(ks,abs(fftshift(ut)),'b',ks,avg2,'k');
    pause(0.5);
end
