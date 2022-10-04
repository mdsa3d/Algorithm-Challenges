# arr = [1,2,3,4,5]
using Combinatorics
function miniMaxSum2(arr)
    val = [sum(c) for c in combinations(arr, 4)]
    return print("$(minimum(val)) $(maximum(val))")
end

function miniMaxSum(arr)
    val = [sum(arr)-arr[i] for i in 1:5]
    return print("$(minimum(val)) $(maximum(val))")
end

arr = map(x -> parse(Int32, x), Array{String}(split(rstrip(readline(stdin)))))

miniMaxSum(arr)