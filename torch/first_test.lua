require 'torch'
torch.manualSeed(1234)
-- choose a dimension
N = 5

-- create a random NxN matrix
A = torch.rand(N, N)

-- make it symmetric positive
A = A*A:t()

-- make it definite
A:add(0.001, torch.eye(N))

-- add a linear term
b = torch.rand(N)

-- create the quadratic form
function J(x)
   return 0.5*x:dot(A*x)-b:dot(x)
end

print(J(torch.rand(N)))

xs = torch.inverse(A)*b
print(string.format('J(x^*) = %g', J(xs)))
function dJ(x)
  return A*x-b
end

-- x = torch.rand(N)
-- lr = 0.01
-- for i=1,20000 do
--   x = x - dJ(x)*lr
--   -- we print the value of the objective function at each iteration
--   print(string.format('at iter %d J(x) = %f', i, J(x)))
-- end

-- with optim
require 'optim'
-- do
--    local neval = 0
--    function JdJ(x)
--       local Jx = J(x)
--       neval = neval + 1
--       print(string.format('after %d evaluations J(x) = %f', neval, Jx))
--       return Jx, dJ(x)
--    end
-- end
evaluations = {}
time = {}
timer = torch.Timer()
neval = 0
function JdJ(x)
   local Jx = J(x)
   neval = neval + 1
   print(string.format('after %d evaluations, J(x) = %f', neval, Jx))
   table.insert(evaluations, Jx)
   table.insert(time, timer:time().real)
   return Jx, dJ(x)
end


-- ## CG loss minimisation ##
state = {
   verbose = true,
   maxIter = 100
}

x0 = torch.rand(N)
cgx = x0:clone() -- make a copy of x0
timer:reset()
optim.cg(JdJ, cgx, state)

-- we convert the evaluations and time tables to tensors for plotting:
cgtime = torch.Tensor(time)
cgevaluations = torch.Tensor(evaluations)

-- ## SGD optimizer ##
evaluations = {}
time = {}
neval = 0
state = {
  lr = 0.1
}

-- we start from the same starting point than for CG
x = x0:clone()

-- reset the timer!
timer:reset()

-- note that SGD optimizer requires us to do the loop
for i=1,1000 do
  optim.sgd(JdJ, x, state)
  table.insert(evaluations, Jx)
end

sgdtime = torch.Tensor(time)
sgdevaluations = torch.Tensor(evaluations)


require 'gnuplot'
gnuplot.figure(1)
gnuplot.plot(
   {'CG',  cgtime,  cgevaluations,  '-'},
   {'SGD', sgdtime, sgdevaluations, '-'})
gnuplot.xlabel('time (s)')
gnuplot.ylabel('J(x)')
