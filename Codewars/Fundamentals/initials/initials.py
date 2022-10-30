def abbrev_name(name):
    nameList = name.split(' ')
    initials = ''
    for i in nameList:
        initials = initials + i[0].upper() + '.'
    return initials[:-1]

def abbrev_name(name):
    return '.'.join(c[0].upper() for i, c in enumerate(name.split(' ')))

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

def abbrevName(name):
    return name.split(' ')[0][0].upper()+'.'+name.split(' ')[1][0].upper()