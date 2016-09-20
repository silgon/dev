using Distributions
# using GaussianMixtures
# g = rand(GMM, 30, 2)
# m = MixtureModel(g)
# srand(5)
srand(7)
mvs = MvNormal[]
n_dims = 2
n_gmm = 30
for _ in 1:n_gmm
    tmp = rand(n_dims, n_dims)
    Σ = tmp*tmp'
    mv = MvNormal(rand(n_dims), Σ)
    push!(mvs,mv)
end
pre_w = rand(n_gmm)
w = pre_w/sum(pre_w)
m = MixtureModel(mvs, w)



x_n= y_n= 50
x = linspace(0, 1, x_n)
y = linspace(0, 1, y_n)
X = repmat(x, 1, y_n)'
Y = repmat(y, 1, x_n)

Z = zeros(X)
for iter in eachindex(X)
    Z[iter] = pdf(m, [X[iter],Y[iter]])
end

using PyCall, PyPlot
@pyimport seaborn as sns
plt = sns.plt
plt[:clf]()
plt[:contour](X, Y, Z, cmap="viridis")
plt[:colorbar]()
