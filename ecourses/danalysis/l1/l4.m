clear all; close all; clc;

%% convergence of signal with a loop and white noise parameter
T=60; % Domain
n=512; % points in the function

t2=linspace(-T/2,T/2,n+1);
t=t2(1:n); % we get rid of the last point because the last point is the same as the first
k=(2*pi/T)*[0:n/2-1 -n/2:-1];
ks=fftshift(k); % shift the function for the fourier transformation

slice=[0:0.5:10];
[T,S]=meshgrid(t,slice);
[K,S]=meshgrid(k,slice);
U=sech(T-10*sin(S)).*exp(i*10*T);
subplot(2,1,1)
waterfall(T,S,abs(U)),colormap([0 0 0]), view(-15,70)

noise=20;
for j=1:length(slice)
    UT(j,:)=fft(U(j,:))+noise*(randn(1,n)+i*randn(1,n));
    UN(j,:)=ifft(UT(j,:));
end
subplot(2,1,2)
waterfall(fftshift(K),S,abs(fftshift(UT))), view(-15,70)
subplot(2,1,1)
waterfall(T,S,abs(UN)), view(-15,70)
