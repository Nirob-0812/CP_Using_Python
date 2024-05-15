n=int(input())
s=str(n)
print('YNEOS'[not ((s.count('4') + s.count('7'))==7 or (s.count('4') + s.count('7'))==4)::2])