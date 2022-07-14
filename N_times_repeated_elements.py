n=int(input())
a=list(map(int,input().split()))
k=int(input())
y=[]
for i in a:
    if a.count(i)==k:
        y.append(i)
if len(y)==0:
    print("-1")
else:
    y=set(y)
    print(*y)