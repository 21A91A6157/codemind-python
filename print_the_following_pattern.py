n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k-1,end="")
    for l in range(1,i):
        print(l,end="")
    print()