a=int(input())
b=list(map(int,input().split()))
pd=1
for i in range(a):
    for j in range(a):
        if b[i]==b[j]:
            continue
        else:
            pd*=b[j]
    print(pd,end=" ")
    pd=1