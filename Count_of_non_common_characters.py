s1=input().lower()
s2=input().lower()
k=set(s1)
k.discard(" ")
p=set(s2)
l=[]
k=((p.symmetric_difference(k)))
l.append(k)
c=0
for i in k:
    if i!=" " and i.isalpha():
        c+=1
print(c)