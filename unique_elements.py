n=int(input())
lst=list(map(int,input().split()))
s=[]
for i in lst:
    if i not in s:
        s.append(i)
print(*s)