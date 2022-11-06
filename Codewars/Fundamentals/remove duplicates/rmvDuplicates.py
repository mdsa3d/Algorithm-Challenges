def unique_in_order(iterable):
    unique = []
    if len(iterable)==1:
        unique.append(iterable)
    if len(iterable)>1: 
        unique.append(iterable[0])
        for i in range(len(iterable)):
            if not iterable[i]==unique[-1]:
                unique.append(iterable[i])
    return unique



# method 2:
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev=char
    return result

# method 3:
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

# method 4:
from itertools import groupby
def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]



# method 5:
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]


print(unique_in_order('AAAABBBCCDAABBB') == ['A','B','C','D','A','B'])
print(unique_in_order([1,2,2,3,3]) == [1,2,3])