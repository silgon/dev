N = 11;
x = [0:0.1:10];
f = zeros(1,size(x,2));
for i = 1:2:N
  a = (1/pi)*(4/(pi*i^2))*(cos((pi*i/2)-1));
  b = (1/pi)*((4/(pi*i^2))*(sin(pi*i/2-1))-2/pi*(cos(pi*i)));
  f = f + a*cos(i*x)+ b*sin(i*x);
end
f = .75 + f;
plot(x,f)
