n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=set(a)
d=set(b)
e=len(c.union(d))
f=len(c.intersection(d))
print(e-f)