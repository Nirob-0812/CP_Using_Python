i=lambda:[*map(int,input().split())]
k,n,w=i()
need=0
while w>0:
    need+=w*k
    w-=1
need-=n
if need>0:
    print(need)
else:
    print(0)

