n=int(input())
l=[]
c=0
lst=list(map(int,input().split()))
for i in range(0,n-2):
    if lst[i+2]==lst[i]+lst[i+1]:
        c=c+1
    else:
        c=0
        break
p=n-2
if c==0:
    print("no")
else:
    print("yes")