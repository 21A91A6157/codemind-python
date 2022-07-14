n=int(input())
a=list(map(int,input().split()))
y=[]
e=[]
for i in a:
    if i%2==0:
        y.append(i)
    else:
        e.append(i)
print(*y,end=' ')
print(*e)
    