n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for num in arr:
    if num<a or num>b:
        l.append(num)
if len(l)==0:
    print("-1")
else:
    m=max(l)
    print(m)
        