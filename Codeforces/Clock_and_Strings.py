k=lambda:[*map(int,input().split())]
n=int(input())
for j in range(n):
    g=False
    h=False
    a,b,c,d=k()
    p=0
    if abs(a-b)>6:
        s=max(a,b)
        e=min(a,b)+12
        for i in range(s,e+1):
            p=i
            if p >12:
                p-=12
            if p==c:
                g=True
            if p==d:
                h=True
    else:
        s=max(a,b)
        e=min(a,b)
        for i in range(e,s+1):
            if i==c:
                g=True
            if i==d:
                h=True
    if (g==False and h==False) or (g==True and h==True):
        print('NO')
    else:
        print('YES')
        