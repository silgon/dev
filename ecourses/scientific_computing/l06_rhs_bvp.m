function rhs=l06_rhs_bvp(x,y)
rhs=[y(2); -3*y(2)-6*y(1)+5];