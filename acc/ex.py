import math
n = int(input())
len = len(str(n))

if len == 1:
    print(n)
elif len > 1:
    if len % 2 == 1 :
        print(math.ceil(n/2))
    else:
        print(math.floor((n-2)/2))
