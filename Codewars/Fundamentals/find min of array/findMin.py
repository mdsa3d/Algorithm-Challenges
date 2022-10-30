def findSmallestInt(arr):
    return min(arr)

def find_smallest_int(arr):
      return sorted(arr)[0]

findSmallestInt=min 

def findSmallestInt(arr):
    small = arr[0]
    for i in arr:
        if i < small:
            small = i
    return small


findSmallestInt = lambda a: sorted(a)[0]