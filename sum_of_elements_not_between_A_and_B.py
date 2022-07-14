n=int(input())
a=list(map(int,input().split()))
k,l=map(int,input().split())
d=[]
for i in a:
    if i<k or i>l:
        d.append(i)
print(sum(d))
        