def calacute_food(r,unit,n,arr):
    if arr is None or n == 0:
        return -1
    
    req_food = r * unit
    foodtillnow = 0

    for i in range(n):
        foodtillnow += arr[i]
        if foodtillnow >= req_food:
            return i+1
    return 0

r = int(input())
unit = int(input("unit : "))
n = int(input())
arr = list(map(int, input().split()))
calacute_food(r,unit,n,arr)