i=lambda:[*map(int,input().split())]
n=int(input())
m=0
s=0
for _ in range(n):
    a,b=i()
    s+=b-a
    m=max(s,m)
print(m)