i=lambda:[*map(int,input().split())]
n,t=i()
s=input()
s=list(s)
for _ in range(t):
    i=0
    while i<len(s)-1:
        if s[i]=='B' and s[i+1]=='G':
            s[i],s[i+1]='G','B'
            i+=2
        else:
            i+=1
print(''.join(s))

        
