n=int(input())
g=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
for i in g:
    if i<a or i>b:
       d.append(i)
if len(d)==0:
    print("-1")
else:
    print(min(d))
    