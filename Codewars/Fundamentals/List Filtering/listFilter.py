def filter_list(l):
    # 'return a new list with the strings filtered out'
    new = []
    for i in l:
        if isinstance(i, str):
            continue
        else:
            new.append(i)
    return new


def filter_list(l):
    return [x for x in l if not isinstance(x, str)] 


def filter_list(l):
    # 'return a new list with the strings filtered out'
    return [x for x in l if type(x) is not str]

filter_list = lambda l: [e for e in l if isinstance(e, int)]