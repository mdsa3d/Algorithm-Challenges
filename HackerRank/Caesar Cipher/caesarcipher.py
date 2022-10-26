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

def caesarCipher(s, h):
    # Write your code here
    a = "abcdefghijklmnopqrstuvwxyz"
    casing=[]
    if h >26:
        n = int(h/26)
        for i in range(n):
            a= a[::-1]
        k = h%26
    else:
        k=k
    k= k-3
    temp = []
    for i, v in enumerate(s):
        if v.isupper():
            casing.append(i)
        pos = ord(v.lower()) - 96
        if 0 <= pos < (26-k):
            pos = pos + k 
            temp.append(a[pos])
        elif 26 >= pos >= (26-k):
            pos = k - (26 - pos)
            temp.append(a[pos])
        elif pos < 0:
            temp.append(v)
    for i in casing:
        temp[i]=temp[i].upper()
    return "".join([str(i) for v,i in enumerate(temp)])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = input()

    # k = int(input().strip())

    # result = caesarCipher(s, k)

    # fptr.write(result + '\n')

    # fptr.close()

    n= 10
    s = "www.abc.xy"
    k=87
    result = caesarCipher(s, k)
    print(result)