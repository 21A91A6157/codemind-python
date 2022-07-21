m=int(input())
n=int(input())
d=0
for i in range(0,m):
    d+=sum(list(map(int,input().split())))
print(d)
    