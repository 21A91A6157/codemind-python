def fun(n):
    res=0
    while n:
        d=n%10
        res+=d
        n=n//10
    return res
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
   s+=fun(i)
print(s)