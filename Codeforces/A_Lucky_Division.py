n=int(input())
s=''.join(set(str(n)))
s_l=len(set(str(n)))
if n%4==0 or n%7==0 or n%47==0 or n%74==0 or n%477==0 or n%774==0 or n%747==0 or (s_l==2 and s=='47') or (s_l==2 and s=='74') or (s_l==1 and s=='4') or (s_l==1 and s=='7'):
    print('YES')
else:
    print('NO')
