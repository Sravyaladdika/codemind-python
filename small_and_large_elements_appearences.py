s=input()
l=[]
for i in s:
    if i!=" ":
        l.append(i)
q=max(l)
p=min(l)
print(p,l.count(p),q,l.count(q))