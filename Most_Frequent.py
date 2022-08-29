n=int(input())
a=list(map(int,input().split()))
b=[]
d=[]
for i in a:
    b.append(a.count(i))
c=max(b)
for i in a:
    if a.count(i)==c:
        d.append(i)
d=set(d)
d=list(d)
d.sort()
print(d[0])