function rhs=l01_shoot(xspan,x,dummy,n0,beta)
rhs=[ x(2)
(beta-n0)*x(1) ];
end

