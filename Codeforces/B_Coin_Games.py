t=int(input())
for i in range(t):
    n=int(input())
    str=input()
    u=0
    for j in str:
        if j=='U':
            u+=1
    if u%2==1:
        print('YES')
    else:
        print('NO')