m=[list(map(int,input().split())) for _ in ' '*5]

r,c=0,0
for i in range(5):
    for j in range(5):
        if m[i][j]==1:
            r,c=i,j
print(abs(r-2)+abs(c-2))
