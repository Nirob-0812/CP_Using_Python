i=lambda:[*map(int,input().split())]
n=int(input())
a=i()
ind=[]
for i in range(1,n+1):
    ind.append(a.index(i)+1)
print(*ind)