def find_it(seq):
    if len(seq) <=1:
        return seq[0]
    else:
        u = list(set(seq))
        for i in u:
            count = 0
            for c in seq:
                if i == c:
                    count += 1
            if not count % 2 == 0:
                return i

# method 2
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

# method 3
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

# method 4
import operator
def find_it(xs):
    return reduce(operator.xor, xs)

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5)