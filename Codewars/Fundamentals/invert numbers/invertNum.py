def invert(lst):
    return [i-(2*i) for i in lst] if lst else []

# method 2
def invert(lst):
    return [-x for x in lst]

# method 3
def invert(lst):
    return list(map(lambda x: -x, lst));

# method 4
def invert(lst):
   return [i*-1 for i in lst]