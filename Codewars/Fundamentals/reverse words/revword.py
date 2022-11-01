def reverse_words(text):
    ntl = ''
    for i in text.split(' '):
        ntl = ntl + i[::-1] + ' '
    return ntl[:-1]

def reverse_words(str):
      #go for it
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)

def reverse_words(text):
    return ' '.join(c[::-1] for i, c in enumerate(text.split(' ')))

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

import re
def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)