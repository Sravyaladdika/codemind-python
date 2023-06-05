n=int(input())
lst=list(map(int,input().split()))
l=[]
k=lst[::2]
for num in k:
    if num%2==0:
        l.append(num)
if len(l)==len(k):
    print("True")
else:
    print("False")
        
