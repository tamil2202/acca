def next_odd(n,arr):
    for i in range(n):
        next = arr[i+1]
        if (next % 2 == 1):
            return (i+1)

n = int(input())

arr = list(map(int, input().split()))

print(next_odd(n,arr))
