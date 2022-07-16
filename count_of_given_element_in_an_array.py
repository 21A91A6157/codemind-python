n=int(input())
a=list(map(int,input().split()))
z=int(input())
c=0
for i in range(n):
    if a[i]==z:
        c+=1
print(c)
    