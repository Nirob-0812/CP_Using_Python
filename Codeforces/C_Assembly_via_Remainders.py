t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    k=[]
    for j in range(n):
        if j==n-1:
            if a[j]==1:
                k.append(3)
            else:
                k.append(a[j])
        elif j==n-2:
            if a[j-1]==1:
                k.append(2)
            else:
                k.append(a[j-1]+1)
        else:
            if a[j-1]==1:
                k.append(2)
            else:
                k.append(a[j-1])
    print(*k)
        
        

