inpolygon(point, polygon) = inpolygon(point[1], point[2], polygon)
function inpolygon(m, n, polygon)
    j = size(polygon)[1]
    oddnodes = false
    M = polygon[:,1]
    N = polygon[:,2]

    for i in 1:size(polygon)[1]
        if M[i] < m && M[j] >= m || M[j] < m && M[i] >= m
            if N[i] + (m-M[i]) / (M[j]-M[i]) * (N[j]-N[i]) < n
                oddnodes = !oddnodes
            end
        end
        j = i
    end

    oddnodes
end


triangle = [0. 0.;
            0. 4.;
            4. 0.]
point = [3.99 0.001]
println(triangle)
println(point)
result = inpolygon(point, triangle)
println(result)
