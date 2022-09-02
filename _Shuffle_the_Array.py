n=int(input())
a=list(map(int,input().split()))
b=[]
x=n//2
for i in range(0,x):
    b.append(a[i])
    b.append(a[i+x])
print(*b)