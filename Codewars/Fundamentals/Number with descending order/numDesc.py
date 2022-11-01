def descending_order(num):
    if num == 0:
        return num
    else:
        n = sorted([int(i) for i in list(str(num))])[::-1]
        return int(''.join(str(i) for i in n))
print(descending_order(15))

# method 2
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

# method 3
def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')