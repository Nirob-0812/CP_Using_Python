s=input()
k=1
c=sum(k for i in s if i.islower())
if c>=(len(s)-c):
    print(s.lower())
else:
    print(s.upper())