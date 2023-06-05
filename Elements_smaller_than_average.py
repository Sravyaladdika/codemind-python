n=int(input())
arr=list(map(int,input().split()))
a=sum(arr)
c=a//n
k=0
for i in range(n):
    if(arr[i]<=c):
        k+=1
print(k)