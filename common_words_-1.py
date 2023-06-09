s1=input().lower().split()
s2=input().lower().split()
p=set(s1)
q=set(s2)
p.discard(" ")
q.discard(" ")
t=(p.intersection(q))
c=0
for i in t:
    c+=1
print(c)
    