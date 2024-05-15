i=lambda:[*map(int,input().split())]
n,k=i()

while k>0:
    if n%10==0:
        n//=10
    else:
        n-=1
    k-=1
print(n)