n,m=map(int,input().split())
a=list(map(int,input().split()))
co=a
c=1
while c<=m:
    x=a[0]
    co.remove(x)
    co.append(x)
    c+=1
print(*co)