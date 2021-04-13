def fib(n):
    cache=[0 for i in range(n+1)]
    cache[1]=1
    for i in range(2,n+1):
        cache[i]=cache[i-1]+cache[i-2]
    return cache[n]

print(fib(1000))
    
