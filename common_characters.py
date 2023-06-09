s1=input().lower()
s2=input().lower()
p=set(s1)
q=set(s2)
p.discard(" ")
q.discard(" ")
i=p.intersection(q)
if i:
    m=list(i)
    m.sort()
    print(''.join(m))
else:
    print("-1")
