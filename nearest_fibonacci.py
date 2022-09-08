def fun(n):
    if n==0:
        print(0)
        return 0
    a=0
    b=1
    c=a+b
    while c<=n:
        a=b
        b=c
        c=a+b
    d=c+b
    if abs(c-n)>abs(b-n):
        print(b)
    elif abs(c-n)>abs(d-n):
        print(d)
    elif abs(c-n)==abs(b-n):
        print(b,c,end=' ')
    else:
        print(c)
n=int(input())
fun(n)