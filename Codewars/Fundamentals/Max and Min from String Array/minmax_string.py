def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split(' ')]
    m = max(numbers)
    n = min(numbers)
    return "{} {}".format(m,n)

def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))