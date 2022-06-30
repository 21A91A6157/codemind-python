n=int(input())
c=0
t=n
while n>0:
    c+=1
    n=n//10
n=t*t
if t==n%(pow(10,c)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    