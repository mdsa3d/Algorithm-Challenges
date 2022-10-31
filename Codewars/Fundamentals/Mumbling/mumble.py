def accum(s):
    l = list(s)
    st = ''
    for i in range(len(l)):
        st = st + l[i].upper() + (l[i].lower()*i)  + '-'
    return st[0:-1]



def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]



def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))

def accum(s):
    a = list(s)
    res = ""
    for i, c in enumerate(a):
        res += c * (i + 1) + "-"
    return res.strip("-").title()

    