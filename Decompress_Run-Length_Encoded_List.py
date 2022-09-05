n=int(input())
a=list(map(int,input().split()))
d=[]
for i in range(0,n,2):
    x=a[i]
    y=a[i+1]
    for i in range(0,x):
        d.append(y)
print(*d)