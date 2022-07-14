n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
y=[]
for i in d:
    if i<a or i>b:
        y.append(i)
if len(y)==0:
    print("-1")
else:
    print(*y)