def alphabet_position(text):
    s=''
    for i in text:
        if i.isalpha():
            s +=str(ord(i.lower())-96) + ' '
    return s[:-1]

# method 2
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# method 3
from string import ascii_lowercase
def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")