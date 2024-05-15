i=lambda:[*map(int,input().split())]
n=int(input())
for j in range(n):
    b,c=i()
    if c<b:
        print(f"{c} {b}")
    else:
        print(f"{b} {c}")
