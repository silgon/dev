using Graphs

# directed graph
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


# graph with comprehension edges
g1ex = graph([i for i in 1:5], ExEdge{Int}[], is_directed=true)

#todo -- this should be doable in a comprehension, I can't get the types to work
for (i,v) in enumerate(g1_wedges)
    ed = ExEdge(i, v[1], v[2])
    ed.attributes["length"] = v[3]
    add_edge!(g1ex, ed)
end



# comprehension vertices-edges graph
CG_VertexList = ExVertex[]
CG_EdgeList = ExEdge{ExVertex}[]

g2ex = graph(CG_VertexList, CG_EdgeList)

v1 = ExVertex(1, "VertexName")
v1.attributes["Att"] = "Test"
v2 = ExVertex(2, "truu")
v2.attributes["Att"] = "Test1"

add_vertex!(g2ex, v1)
add_vertex!(g2ex, v2)
ed = ExEdge(1, v1, v2)
ed.attributes["length"] = 10
add_edge!(g2ex, ed)

type VertexGraph
    id::UInt32
    S::Array{Float64,1}
    V::Float64
    function VertexGraph(id::Integer)
        new(id, Float64[0], 0)
    end
end

type EdgeGraph{V} 
    id::UInt32
    source::V
    target::V
    Q::Float64
    action::Array{Float64, 1}
    ap::Array{Float64, 1}
    function EdgeGraph(id::Integer, source::V, target::V)
        new(id, source, target, 0, [0], [0])
    end
end

edge_index(e::EdgeGraph) = e.index
source(e::EdgeGraph) = e.source
target(e::EdgeGraph) = e.target
source{V}(e::EdgeGraph{V}, g::AbstractGraph{V}) = e.source
target{V}(e::EdgeGraph{V}, g::AbstractGraph{V}) = e.target
attributes(e::EdgeGraph, g::AbstractGraph) = e.attributes


g = graph(VertexGraph[], EdgeGraph{VertexGraph}[])
v = [VertexGraph(i) for i=1:10]
for i=1:size(v)[1]
    add_vertex!(g, v[i])
end
for i=1:size(v)[1]-1
    add_edge!(g, EdgeGraph{VertexGraph}(i, v[i], v[i+1]))
end
println(g)
