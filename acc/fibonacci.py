def fibo(n):
    if (n==0):
        return []
    elif (n==1):
        return 0
    elif (n==2):
        return[0,1]
    
    fibo_seq = [0,1]
    for i in range(2,n):
        next = fibo_seq[-2] + fibo_seq[-1]
        fibo_seq.append(next)
    return fibo_seq

n = int(input())
print(fibo(n))
            
