def reverse_seq(n):
    return [x+1 for x in range(n)][::-1]


# method 2
def reverseseq(n):
    return [x for x in range(n,0,-1)]

# method 3
def reverseseq(n):
    return list(range(n, 0, -1)) # range(start, end, step)

# method 4
def reverseseq(n):
    return range(n, 0, -1)