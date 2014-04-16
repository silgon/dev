%% fourier transform image

clear all; close all; clc;
A=imread('london.jpg'); % read image
Abw=rgb2gray(A); % convert to black and white
Abw=double(Abw); % convert to double precision
% image(Abw) %% check image

% add noise to the picture
Abwn= Abw+100*randn(size(Abw));

figure(1)
pcolor(rot90(Abwn,2)), shading interp, colormap hot
figure(2)
Abwt=fft2(Abwn); % fourier transform
pcolor(log(abs(fftshift(Abwt)))), shading interp
