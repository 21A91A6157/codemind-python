n=int(input())
a=list(map(int,input().split()))
cc=0
for i in range(0,n):
    if a[i]%2==0:
        if i%2!=0:
            cc=1
            print(False)
            break
if cc==0:
    print(True)