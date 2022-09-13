def fun(i):
    c=0
    if i<0:
        i=-i
    if i==0:
        return 1
    while i:
        c+=1
        i=i//10
    return c
n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    d.append(fun(i))
print(*d)

    