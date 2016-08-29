import JSON

dict1 = Dict("param1" => 1, "param2" => 2,
            "dict" => Dict("d1"=>1.,"d2"=>1.,"d3"=>1.))

stringdata = JSON.json(dict1)

open("write_read.json", "w") do f
        write(f, stringdata)
     end

dict2 = Dict()
open("write_read.json", "r") do f
    global dict2
    dicttxt = readall(f)
    dict2=JSON.parse(dicttxt)
end

println(dict1)
println(dict2)

