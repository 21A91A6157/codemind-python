a=int(input())
x=list(map(int,input().split()))
b=int(input())
y=list(map(int,input().split()))
c=[]
for i in range(a):
    c.insert(y[i],x[i])
print(*c)