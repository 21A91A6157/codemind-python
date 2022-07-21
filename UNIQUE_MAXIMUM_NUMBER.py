n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    if a.count(i)==1:
        d.append(i)
if len(d)==0:
    print("-1")
else:
    print(max(d))
        