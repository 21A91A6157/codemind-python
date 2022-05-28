n=int(input())
t=n
sum=0
while(n):
    f=1
    r=n%10
    for i in range(r,0,-1):
        f=f*i
    sum+=f
    n=n//10
if sum==t:
    print('The number',t,'is a strong number')
else:
    print('The number',t,'is not a strong number')