using Printf:@printf
function plusMinus(arr)
    n = size(arr,1)
    count_pos = 0
    count_neg = 0
    count_zero = 0
    for i in 1:n
        if  arr[i] > 0
            count_pos = count_pos+1
        elseif arr[i]<0
            count_neg = count_neg+1
        else
            count_zero = count_zero+1
        end
    end
    pos_ratio, neg_ratio, zero_ratio = count_pos/n, count_neg/n, count_zero/n
    vec = [pos_ratio, neg_ratio, zero_ratio]
    [@printf "%6f\n" f for f in vec]
    return nothing
end 

n = parse(Int32, strip(readline(stdin)))

arr = map(x -> parse(Int32, x), Array{String}(split(rstrip(readline(stdin)))))

plusMinus(arr)