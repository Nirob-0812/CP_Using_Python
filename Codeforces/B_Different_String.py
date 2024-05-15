import random
n=int(input())
for i in range(n):
    s=input()
    if len(set(s))<2:
        print('NO')
    else:
        print('YES')
        r=s[:1]
        p=s[1:]
        print(p+r)