n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=a
c=1
while c<=m:
    x=b[-1]
    b.insert(0,x)
    b.pop()
    c+=1
print(*b)
