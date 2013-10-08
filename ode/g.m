function xdot=g(vt,vy) 
  xdot=[vy(2); (1 - vy(1)^2) * vy(2) - vy(1)];
end
