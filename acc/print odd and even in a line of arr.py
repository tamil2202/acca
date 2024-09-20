arr = list(map(int, input().split()))
sort=[]
odd=[]
for i in arr:
    if (i % 2 == 0):
        sort.append(i)
print(sort)

for j in arr:
    if (j % 2 == 1):
        odd.append(j)
print(odd)

print(odd+sort)
