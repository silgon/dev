# usage: julia -p 4 parallel.jl

# everywhere shall be used to load function in all the processes
@everywhere function count_heads(n)
    c::Int = 0
    for i=1:n
        c += rand(Bool)
    end
    n, c  # tuple (input, output)
end

v=pmap(count_heads, 50000:1000:70000)
println("Pmap counting heads")
println(v)

# println("parallel for counting heads")
@sync @parallel for i in 50000:1000:70000
    println(count_heads(i))
end
# sleep(10)

@everywhere using Graphs
println("Pmap erdos graph")
# erg = pmap(erdos_renyi_graph, 500:100:1000, .2)
r_values = 500:100:1000
# option 1
# erg = pmap((a1,a2)->erdos_renyi_graph(a1,a2), r_values, ones(length(r_values))*.2)
# option 2
erg = pmap((args)->erdos_renyi_graph(args...), zip(r_values, ones(length(r_values))*.2))

println(erg)
