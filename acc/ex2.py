import math
s, p =map(int, input().split())

if s < p:
    print(math.ceil(p/s))