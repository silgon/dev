%% filtering signal

clear all; close all; clc;
A=imread('london.jpg'); % read image
Abw=rgb2gray(A); % convert to black and white
A3=Abw; % variable for imshow
Abw=double(Abw); % convert to double precision
Abw=Abw+50*randn(size(Abw)); % noise
Abwt=fftshift(fft2(Abw));
A1=uint8(Abw);
pcolor(log(abs(Abwt))), shading interp, colormap hot

% Filter
kx=1:size(Abw,2); ky=1:size(Abw,1);
[KX,KY]=meshgrid(kx,ky);
sigma=0.0001; % the size of the filter is going to affect what we keep from the transformed image
F=exp(-sigma*(KX-size(Abw,2)/2+1).^2 - sigma*(KY-size(Abw,1)/2+1).^2);
pcolor(F), shading interp, colormap hot

% Filter * Image
Abwtf=Abwt.*F;
Abwf=ifft2(fftshift(Abwtf));
A2=uint8(real(Abwf)); % in octave real is needed because they are some complex numbers
subplot(1,3,1), imshow(A1)
subplot(1,3,2), imshow(A2)
subplot(1,3,3), imshow(A3)
