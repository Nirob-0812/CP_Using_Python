n=int(input())

c=0
while n>0:
    if n>=5:
        c+=n//5
        n=n-c*5
    if n>=4:
        c+=n//4
        n=n-c*4
    if n>=3:
        c+=n//3
        n=n-c*3
    if n>=2:
        c+=n//2
        n=n-c*2
    if n>=1:
        c+=n//1
        n=n-c*1

print(c)