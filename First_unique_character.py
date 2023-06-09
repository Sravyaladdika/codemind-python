s=input().lower()
l=[]
for i in s:
    if s.count(i)==1:
        l.append(i)
        print(*l)
        break
else:
    print("-1")