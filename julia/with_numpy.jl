# wrapper library
using PyCall

# import math library from  python
@pyimport math
a = math.sin(math.pi / 4) - sin(pi / 4)  # returns 0.0

println("Printing first example with math library $a")

# import numpy random library
@pyimport numpy.random as nr

A = diagm(collect(0:5:40))
B = nr.randn(size(A)...)  # ... is to pass the tupple as arguments
# multiplying matrix generated with julia and numpy
C = A*B

# print results
println("A")
println(A)
println("B")
println(B)
println("AxB")
println(C)
