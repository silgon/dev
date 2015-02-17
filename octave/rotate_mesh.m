sigma = 4;
[x,y] = deal(-3*sigma:.5:3*sigma);
[X,Y] = meshgrid(x,y);
B = [transpose(x) transpose(y)];

for i=1:1:16
  theta = i*pi/8;
  rotation = [cos(theta) -sin(theta); sin(theta) cos(theta)];
  X1 = reshape(X, length(x)*length(x), 1);
  Y1 = reshape(Y, length(y)*length(y), 1);
  B2 = [X1 Y1];
  A = B2 * rotation;
  X1 = A(:,1);
  X1 = reshape(X1, length(x), length(x));
  Y1 = A(:,2);
  Y1 = reshape(Y1, length(y), length(y));
  mesh(X1, Y1, X1.^2+Y1.^2);
  pause(0.5)
end
