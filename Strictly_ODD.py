n=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    if lst[i]%2!=0:
        if i%2==0:
            print("False")
            break
else:
    print("True")