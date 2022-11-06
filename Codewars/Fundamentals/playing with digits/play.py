def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += int(i)**p
        p+=1
    k=1
    while True:
        val = n*k
        if val == sum:
            return k
            break
        elif val > sum:
            return -1
            break
        k+=1
    # return 1 if sum==n else -1

# method 2
def dig_pow(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c),p+i)
    return s/n if s%n==0 else -1

# miscellenous
def dig_pow(n, p):
    t = sum( int(d) ** (p+i) for i, d in enumerate(str(n)) )
    return t//n if t%n==0 else -1


# method 3
def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k    




print(dig_pow(46288, 3))