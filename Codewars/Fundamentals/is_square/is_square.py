def is_square(n):
    return True if n**0.5 * n**0.5 == n or n==0 else False

def is_square(n):
    return n>=0 and (n**0.5) % 1 == 0
    
def is_square(n):
    if n>=0:
        if int(n**0.5)**2 == n:
            return True
    return False

import math
def is_square(n):
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False

import math
def is_square(n):
    if n<0:
        return False
    return math.sqrt(n).is_integer()