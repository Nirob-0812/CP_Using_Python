n,k=map(int,input().split())
count=0
a=[int(x) for x in input().split()]
for i in range(n):
    if a[i]>=a[k-1] and a[i]>0:
        count+=1
print(count)