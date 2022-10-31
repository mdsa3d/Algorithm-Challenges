import string
toJadenCase = string.capwords

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


def to_jaden_case(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)


def to_jaden_case(string):
    return ' '.join(map(str.capitalize, string.split()))