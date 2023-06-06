import math 
def isprime(n):
    s=int(math.sqrt(n))
    if n<2:
        return False
    for i in range(2,s+1):
        if n%i==0:
            return False
    return True
def ispalindrome(n):
    while True:
        n=n+1
        p=str(n)
        if isprime(n):
            if p==p[::-1]:
                return p
                break
        else:
            n=int(p)
n=int(input())
print(ispalindrome(n))