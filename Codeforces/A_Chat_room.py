s=input()
k=0
cnt=0
for i,c in enumerate('hello'):
    for j in range(k,len(s)):
        if s[j]==c:
            k=j+1
            cnt+=1
            break
if cnt==5:
    print('YES')
else:
    print('NO')



