n=int(input())
a=list(map(int,input().split()))
c=0
b=set(a)
for i in b:
    if i%2==0:
        c=c+1
print(c)