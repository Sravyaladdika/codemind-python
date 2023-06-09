def count(n):
    p=max(n)
    q=min(n)
    return abs(ord(p)-ord(q))
s=input().split()
p=list(s)
for i in p:
    print(count(i),end=' ')