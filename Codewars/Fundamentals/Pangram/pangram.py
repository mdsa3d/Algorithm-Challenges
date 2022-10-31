import string
alphabet = set(string.ascii_lowercase)
def is_pangram(s):
    return set(s.lower()) >= alphabet


# method 2
import string
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


# method 3
import string
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())

# method 4
def is_pangram(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False


# method 5
def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))
   