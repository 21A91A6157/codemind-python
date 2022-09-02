t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k=sorted(a)
    if k==a:
        print(0)
    else:
        print(k[-1]-k[0])
    