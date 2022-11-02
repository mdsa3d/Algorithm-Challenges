a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def longest(a1, a2):
    a = sorted(a1+a2)
    s = []
    for i in a:
        if i not in s:
            s.append(i)
    return ''.join(s)

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))
    
print(longest(a, b) == "abcdefklmopqwxy")