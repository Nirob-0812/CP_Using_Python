i=lambda:[*map(int,input().split())]
n,h=i()
c=0
a=i()
for i in a:
    if i>h:
        c+=1

print(n+c)