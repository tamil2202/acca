def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

n = int(input())

arr = list(map(int, input().split()))

odd = []
even = []
for i in range(1,n+1):
    if (i % 2 == 0):
        even.append(i)
    elif (i % 2 == 1):
        odd.append(i)
    else:
        print(0)

sum_even = sum(even)
sum_odd = sum(odd)
print(even)
print(odd)
print("Even index position sum",sum_odd)
print("Odd index position sum",sum_even)