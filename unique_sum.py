n=int(input())
a=list(map(int,input().split()))
a=set(a)
a=list(a)
d=[]
for i in a:
    d.append(i)
print(sum(d))
    