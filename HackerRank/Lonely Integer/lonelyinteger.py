import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    # check one by one
    output = list(set(a))
    for u in output:
        count = 0
        for i in range(len(a)):
            if u == a[i]:
                count = count + 1   
        if count > 1:
            count=0
            continue
        elif count == 1:
            return u

        
        

if __name__ == '__main__':

    n = 3

    a = [1, 2,3 ,4, 3, 2, 1]

    result = lonelyinteger(a)