
def row_sum_odd_numbers(n):
    start = n**2 - (n-1)
    s = start
    for i in range(n-1):
        print(f'value {i+1} = {start}')
        new = start+2
        s += new
        start = new
    print(f'sum is {s}')
    return s

def row_sum_odd_numbers(n):
    return n ** 3


def row_sum_odd_numbers(n):
    if type(n)==int and n>0:
        return n**3
    else:
        return "Input a positive integer"
        
print(row_sum_odd_numbers(1) == 1)
print(row_sum_odd_numbers(2) == 8)
print(row_sum_odd_numbers(3) == 27)
print(row_sum_odd_numbers(4) == 64)