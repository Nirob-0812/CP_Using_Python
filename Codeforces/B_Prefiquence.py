t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=input()
    b=input()
    i,j=0,0
    while i<n and j<m:
        if a[i]==b[j]:
            i+=1
        j+=1
    print(i)