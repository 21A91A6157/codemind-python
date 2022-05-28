t=int(input())
n=abs(t)
res=0
while(n):
    d=n%10
    res=(res*10)+d
    n=n//10
if t<0:
    print(-res)
else:
    print(res)