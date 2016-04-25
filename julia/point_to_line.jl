p = [2,2]
#ax+by+c=0
a=3
b=2
c=3
result = abs(a*p[1]+b*p[2]+c)/sqrt(a^2+b^2)
println(result)

# y=bx+c
bb = a/b
cc = c/b
result2 = abs(p[1]*bb+p[2]+cc)/sqrt(1+bb^2)
println(result2)
