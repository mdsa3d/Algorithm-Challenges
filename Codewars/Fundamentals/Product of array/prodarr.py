def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product

# method 2
from functools import reduce
def grow(arr):
    return reduce(lambda x, y: x * y, arr)

# method 3
import math
def grow(arr):
    return math.prod(arr)


# method 4
from functools import reduce
from operator import mul
def grow(arr):
    return reduce(mul, arr, 1)


# method 5
from math import prod as grow