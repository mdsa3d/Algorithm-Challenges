def fake_bin(x):
    a = list(x)
    for i,c  in enumerate(a):
        if int(c) < 5:
            a[i] = '0'
        else:
            a[i] ='1'
    return ''.join(a)

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


import string
def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))


def fake_bin(x):
    map = str.maketrans('123456789', '000011111')
    return x.translate(map)
    
print(fake_bin("45385593107843568") == "01011110001100111")
