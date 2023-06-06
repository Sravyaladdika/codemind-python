n=int(input())
lst=list(map(int,input().split()))
s=0
l=set(lst)
for i in l:
    if i%2==0:
        s=s+i
print(s)