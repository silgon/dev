# if needed run julia as follows:
# $ LD_PRELOAD=/usr/lib/liblapack.so.3 julia 
using PyCall, PyPlot
@pyimport seaborn as sns
# plot(linspace(0,10,50), linspace(0,10,50))
sns.rugplot(randn(30))
