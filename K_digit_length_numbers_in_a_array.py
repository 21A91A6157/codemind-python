n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    d=str(i)
    if i<0:
        if len(d)-1==k:
            c+=1
    else:
        if len(d)==k:
            c+=1
print(c)