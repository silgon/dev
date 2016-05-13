using Iterators

function expCombination(vals::AbstractArray, order::Int; all::Bool=false)
    @assert order>0 "order must be more than 0"
    tmp = collect(product(repeated(0:order,length(vals))...))
    new_vals = Float64[]
    for t=tmp
        if !((!all & (sum(t)==order)) | (all & (0<sum(t)<=order)))
            continue
        end
        print(t)
        println(": ",vals.^collect(t))
    end
end


a = [2,3,5]

expCombination(a, 3, all=false)
