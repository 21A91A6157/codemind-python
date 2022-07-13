n=int(input())
a=list(map(int,input().split()))
k=int(input())
x=0
for i in a:
    if i<=k:
        x+=i
print(x)