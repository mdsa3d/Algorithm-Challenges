import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.1
#

# def countingSort(arr):
#     # Write your code here
#     output = list(set(arr))
#     n = len(arr)
#     z = [0] * (n+1)
#     for i in range(n):
#         z[arr[i]] = z[arr[i]] + 1
#     # while z:
#     #     if z[-1] != 0:
#     #         break
#     #     del z[-1]
#     return z[0:len(output)]

def countingSort(arr, n):
    z = [0] * (max(arr)+1)
    for i in arr:
        z[i] = z[i] + 1
    return z

if __name__ == '__main__':

    # arr = [1,1,3,2,1]

    # result = countingSort(arr)
    # print(result)
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr, n)
    print(result)