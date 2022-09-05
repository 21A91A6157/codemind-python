n=int(input())
a=list(map(int,input().split()))
c=0
d=[]
for i in a:
    if i==1:
        c+=1
    else:
        d.append(c)
        c=0
d.append(c)
print(max(d))