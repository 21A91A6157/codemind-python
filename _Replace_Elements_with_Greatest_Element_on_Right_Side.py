n=int(input())
a=list(map(int,input().split()))
b=[]
d=[]
for i in a:
    b.append(i)
for i in a:
    b.remove(i)
    if len(b)==0:
        d.append(-1)
    else:
        c=max(b)
        d.append(c)
print(*d)
        