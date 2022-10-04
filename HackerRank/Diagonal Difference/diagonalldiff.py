import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    diag1 = []
    diag2 = []
    for i in range(n):
        diag1.append(arr[i][i])
        diag2.append(arr[i][n-1-i])
    return abs(sum(diag1) - sum(diag2))

if __name__ == '__main__':

    # n = int(input().strip())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(arr)
    print(result)