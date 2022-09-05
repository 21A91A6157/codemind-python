n=int(input())
a=list(map(int,input().split()))
b=0
c=0
for i in range(n):
    if i%2==0:
        b+=a[i]
    else:
        c+=a[i]
if (abs(b)-abs(c))%4==0:
    print("X")
else:
    print("Y")
        