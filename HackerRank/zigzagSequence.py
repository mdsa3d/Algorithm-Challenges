def findZigZagSequence(a, n):
    a.sort()
    mid = int(n/2)
    print(a[mid])
    a[mid], a[n-1] = a[n-1], a[mid]
    print(a)
    st = mid + 1 
    ed = n-2
    while(st < ed):
        a[st], a[ed] = a[ed], a[st]
        print(a[st])
        print(a[ed])
        st = st + 1
        ed = ed - 1
    print(a)
    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)