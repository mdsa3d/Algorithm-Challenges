
function fizzBuzz(n)
    # Write your code here
    for i in 1:n
        j, k = i%3, i%5
        if  j==0 && k==0
            println("FizzBuzz")
        elseif j==0 && k!=0
            println("Fizz")
        elseif k==0 && j!=0
            println("Buzz")
        else
            println(i)
        end
    end
end

n = parse(Int32, strip(readline(stdin)))

fizzBuzz(n)