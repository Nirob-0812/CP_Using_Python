i=lambda:[*map(int,input().split())]
n=int(input())
c=0
for _ in range(n):
    a,b=i() 
    if a+2<=b:
        c+=1
print(c)