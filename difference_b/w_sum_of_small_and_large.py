s=list((input().lower()).split())
a=b=0
for i in s:
    a+=ord(min(i))
    b+=ord(max(i))
print(abs(a-b))