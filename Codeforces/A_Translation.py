t=input()
s=input()
s=list(s)
if t==''.join(s[::-1]):
    print('YES')
else:
    print('NO')
