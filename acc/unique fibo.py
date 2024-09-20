def fibo(n):
    if n <= 1:
        return n
    
    elif n == 2:
        return [0,1]
    
    else:
        fibo_seq = [0,1,1]
        next = []
        for next in range(3,n):
            next = fibo_seq[-3] + fibo_seq[-2] + fibo_seq[-1]
            fibo_seq.append(next)
        return fibo_seq
            

    
n = int(input())
print(fibo(n))