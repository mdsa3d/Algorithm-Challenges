def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr), 2)

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit

    return s
    
     
print(binary_array_to_number([1,1,1,1,1]))