def series_sum(n):
    if n == 1:
        return "1.00"
    elif n == 0:
        return "0.00"
    s = 1
    denom = 4
    for i in range(n-1):
        s += 1/denom
        denom += 3
    return "{:.2f}".format(s)


def series_sum(n):
    if n == 1 or n == 0:
        return "{:.2f}".format(n)
    s = 1
    denom = 4
    for i in range(n-1):
        s += 1/denom
        denom += 3
    return "{:.2f}".format(s)


def series_sum(n):
    if n == 1 or n == 0:
        s = n
    else:
        s = 1
        denom = 4
        for i in range(n-1):
            s += 1/denom
            denom += 3
    return "{:.2f}".format(s)

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum