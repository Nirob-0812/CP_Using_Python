t=int(input())
p=0
for i in range(t):
    a,b,c=map(int,input().split())
    if a+b+c>1:
        p+=1
print(p)
