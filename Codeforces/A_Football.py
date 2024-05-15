s=input()
m=0
b=False
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        m+=1
        if m>5:
            b=True
            break
    else:
        m=0
if b:
    print('YES')
else:
    print('NO')
     