#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def get_pos(s):
    pos = []
    casing= []
    for i, v in enumerate(s):
        if v.isupper():
            casing.append(i)
        pos.append(ord(v.lower()) - 96)
    return pos, casing

def caesarCipher(s, k):
    # Write your code here
    pos_s, casing_s = get_pos(s)
    a = "abcdefghijklmnopqrstuvwxyz"
    shift = (len(a)-(k+1))
    rotate_a = a[shift:] + a[0:shift]
    temp=s
    for i in range(len(s)):
        if pos_s[i] < 0:
            val = s[i]
        elif pos_s[i] >= 0:
            t= pos_s[i]-26
            val = rotate_a[t]
        print(val)
        if pos_s[i] in casing_s:
            val=val.upper()
        temp = temp.replace(temp[i], val)
    return temp #"".join([str(i) for v,i in enumerate(temp)])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = input()

    # k = int(input().strip())

    # result = caesarCipher(s, k)

    # fptr.write(result + '\n')

    # fptr.close()

    n= 11
    s = "middle-Outz"
    k=2
    result = caesarCipher(s, k)
    print(result)