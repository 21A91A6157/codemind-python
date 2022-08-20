n=int(input())
a=list(map(int,input().split()))
res=0
n=n-1
for i in a:
    if i==1:
        res+=(2**n)
    n-=1
print(res)