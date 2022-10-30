def add_binary(a,b):
    return bin(a+b).replace('0b', '')

def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary(a,b):
    """Adds a and b together and returns a binary string"""
    return bin(a + b)[2::]
    
def add_binary(a,b):
    return '{0:b}'.format(a + b)

def add_binary(a, b):
    return format(a + b, 'b')