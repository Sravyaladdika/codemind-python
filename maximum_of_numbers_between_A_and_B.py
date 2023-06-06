n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
for i in lst:
    if i>=a and i<=b:
        m.append(i)
if len(m)==0:
    print("-1")
else:
    print(max(m))