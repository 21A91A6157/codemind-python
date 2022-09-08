n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
for i in a:
    if k==a.count(i) and i not in b:
        b.append(i)
if len(b)==0:
    print("-1")
else:
    print(*b)