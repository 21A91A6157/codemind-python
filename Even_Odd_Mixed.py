n=int(input())
ec=0
oc=0
x=n
rem=0
while n:
    d=n%10
    if d%2==0:
        ec+=1
    else:
        oc+=1
    n=n//10
if ec>0 and oc==0:
    print('Even')
elif oc>0 and ec==0:
    print('Odd')
else:
    print('Mixed')
        
    