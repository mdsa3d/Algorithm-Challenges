
# import math
# import random
# import re

import math
import os
import random
import re
import sys
# def gridChallenge(grid):
#     # Write your code here
#     newgrid = []
#     resp = []
#     if all(isinstance(s, str) for s in grid):
#         for i in range(len(grid)):
#             val = ''.join(sorted(grid[i]))
#             print(val)
#             newgrid.append(val)
#         if newgrid == sorted(newgrid):
#             resp.append('YES')
#     else:
#         resp.append('NO')
#     return resp

# def gridChallenge(grid):
#     # Write your code here
#     return 'YES' if grid == sorted(grid) else 'NO'

# def gridChallenge(grid):
#     newgrid = []
#     while True:
#         for i in range(len(grid)):
#             val = ''.join(sorted(grid[i]))
#             print(val)
#             newgrid.append(val)
#         return 'YES'
#         break
#     else:
#         return 'NO'

# def gridChallenge(grid):
#     # check row can be sorted
#     sortgrid = []
#     colgrid = []
#     gridlen = []
#     for i in range(len(grid)):
#         val = ''.join(sorted(grid[i]))
#         print(val)
#         sortgrid.append(val)
#         n=len(grid[i])
#         gridlen.append(n)
#         for j in range(n):
#             colgrid.append(grid[i][j])
#     newgrid = []
#     for i in range(len(gridlen)):
#         newgrid.append(''.join(grid[i:i+n-1]))

#     if newgrid == sorted(newgrid):
#         return 'YES'
#     else:
#         return 'NO'
#     # # check the columns are in alphabet order
#     # if yes then return 'YES' else 'NO'
#     # pass
def istrue(a):
    if a:
        return True
    else:
        return False


def gridChallenge(grid):
    # check row can be sorted
    mat = [list(i) for i in grid]
    sortgrid = [''.join(sorted(i)) for i in grid]
    sortmat = 
    # colgrid = []
    # gridlen = []
    for i in range(len(mat)):
        
    # newgrid = []
    # for i in range(len(gridlen)):
    #     newgrid.append(''.join(grid[i:i+n-1]))

    # if istrue(sorted(newgrid)) and sorted(newgrid) == sortgrid:
    #     return 'YES'
    # else:
    #     return 'NO'
    # # check the columns are in alphabet order
    # if yes then return 'YES' else 'NO'
    # pass

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
result = gridChallenge(grid)
print(result)


# if __name__ == '__main__':

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         grid = []

#         for _ in range(n):
#             grid_item = input()
#             grid.append(grid_item)

#         result = gridChallenge(grid)
#         print(result)