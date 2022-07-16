n=int(input())
a=list(map(int,input().split()))
av=n//2
for i in a:
    if i==av:
        print("True")
        break
else:
    print("False")