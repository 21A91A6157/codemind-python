x=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
d=[]
for i in a:
    if i>=m and i<=n:
        d.append(i)
if len(d)==0:
    print("-1")
else:
    print(*d)
        