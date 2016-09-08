using JLD, HDF5

jldopen("test.jld", "w") do file
    g = g_create(file, "mygroup") # create a group
    g["dset1"] = 3.2              # create a scalar dataset inside the group
    g["dset2"] = rand(2,2)
end

jldopen("test.jld", "r") do file
    a=read(file, "mygroup")
    println(a)
end


# save graph

using Graphs
g1 = simple_inclist(5)

g1_wedges = [
    (1, 2, 10.),
    (1, 3, 5.),
    (2, 3, 2.),
    (3, 2, 3.),
    (2, 4, 1.),
    (3, 5, 2.),
    (4, 5, 4.),
    (5, 4, 6.),
    (5, 1, 7.),
    (3, 4, 9.) ]

ne = length(g1_wedges)
eweights1 = zeros(ne)
for i = 1 : ne
    we = g1_wedges[i]
    add_edge!(g1, we[1], we[2])
    eweights1[i] = we[3]
end

jldopen("test.jld", "w") do file
    g = g_create(file, "graph") # create a group
    g["dset1"] = g1              # paste graph
end

jldopen("test.jld", "r") do file
    g=read(file, "graph")
    println(g)
end

