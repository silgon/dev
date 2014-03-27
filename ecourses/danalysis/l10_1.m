clear all; close all; clc;
%% Gabor
L=10; n=2048;
t2=linspace(0,L,n+1); t=t2(1:n);
k=(2*pi/L)*[0:n/2-1 -n/2:-1]; ks=ifftshift(k);

S=(3*sin(2*t)+0.5*tanh(0.5*(t-3))+0.28*exp(-(t-4).^2) +1.5*sin(5*t)...
    +4*cos(3*(t-6).^2))/10+(t/20).^3; % signal with a lot of frequencies
St=fft(S);

width=1; % width of the window
slide=0:0.1:10; % sliding the window
spec=[]; % spectogram
for j=1:length(slide)
   f=exp(-width*(t-slide(j)).^2); % filter function
   Sf=f.*S; % filter
   Sft=fft(Sf); % fft of the filter
   
   spec=[spec; abs(fftshift(Sft))];
   
   subplot(3,1,1), plot(t,S,'k',t,f,'m')
   subplot(3,1,2), plot(t,Sf,'k')
   subplot(3,1,3), plot(ks,abs(fftshift(Sft))/max(abs(fftshift(Sft))),'k');
   axis([-60 60 0 1])
   drawnow
   pause(0.1)
end

figure(2)
pcolor(slide,ks,spec.'), shading interp
set(gca,'ylim',[-60 60])
colormap(hot)
xlabel('t')
ylabel('omega')
colorbar


