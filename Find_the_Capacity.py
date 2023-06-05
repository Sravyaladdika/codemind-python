s,t,b=map(int,input().split())
capacity=2*s*t*b*512
c_k_b=capacity//1024
print(str(c_k_b)+"KB")