n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
s=0
for i in lst:
    if i>=a and i<=b:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(sum(l))
        