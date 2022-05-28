n=int(input())
for i in range(1,n+1):
    t=int(input())
    temp=t
    res=0
    while(t):
        d=t%10
        res=(res*10)+d
        t=t//10
    if res==temp:
        print("True")
    else:
        print("False")