using Dates
d ="07:05:45PM"
function timeConversion(s)
    h = parse(Int64, s[1:2])
    if (s[end-1:end] == "PM" && h != 12)
        return string(h+12,":",s[4:8])
    elseif (s[end-1:end] == "AM" && h == 12)
        return string("00",":",s[4:8])
    end
    return s[1:8]
end

fptr = open(ENV["OUTPUT_PATH"], "w")

s = readline(stdin)

result = timeConversion(s)

write(fptr, result * "\n")

close(fptr)