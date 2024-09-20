def evenodd(arr):
    result=""
    for j in arr:
        if(j%2==0):
            result += "EVEN"
        else:
            result += "ODD"
    return(result)

arr = list(map(int, input().split()))

n = int(input())

print(evenodd(arr))
