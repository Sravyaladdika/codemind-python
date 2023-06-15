n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    if a[i]<0:
        a[i]*=-1
a.sort()
for i in a:
    print(i*i,end=' ')
    