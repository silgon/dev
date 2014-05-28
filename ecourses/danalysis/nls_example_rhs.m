function rhs=nls_example_rhs(t,ut,k)
u=ifft(ut);
rhs=-(1i/2)*(k.^2).*ut+1i*fft((abs(u).^2).*u);