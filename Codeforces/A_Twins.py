i=lambda:[*map(int,input().split())]
n=int(input())
a=i()
a=sorted(a,reverse=True)
h=sum(a)//2
c,cnt=0,0
while c<h+1:
    c+=a[cnt]
    cnt+=1
print(cnt)
