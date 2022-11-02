def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c)-96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word

def high(x):
    s, n = x.split(), [sum(ord(c) - 96 for c in y) for y in x.split()]
    return s[n.index(max(n))]
    
print(high('man i need a taxi up to ubud') == 'taxi')
print(high('bb d')== 'bb')