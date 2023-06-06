def isprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
              break
        else:
            return n
m=int(input())
k=int(input())
r=k+m
g=isprime(r)
print(g-r)