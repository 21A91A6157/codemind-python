n=int(input())
g=list(map(int,input().split()))
a,b=map(int,input().split())
e=[]
for i in g:
    if i<a or i>b:
        e.append(i)
if len(e)==0:
    print("-1")
else:
    print(max(e))
        