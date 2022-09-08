n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if a.count(i)==i and i not in b:
        b.append(i)
if len(b)==0:
    print("-1")
else:
    c=(sum(b)/len(b))
    print("{0:.2f}".format(c))