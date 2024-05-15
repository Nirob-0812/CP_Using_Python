i=lambda:[*map(int,input().split())]
n,k=i()
a=[i for i in range(1,n+1,2)]
b=[i for i in range(2,n+1,2)]
c=a+b
print(c[k-1])