def repeat(n,p):
    l=[]
    for i in range(p):
        l.append(n)
    return l
n=int(input())
li=list(map(int,input().split()))
m=[]
for i in range(0,len(li)-1):
    t=(repeat(li[i],li[i+1]))
    m.append(t)
for i in range(0,len(m),2):
    print(*m[i],end=" ")