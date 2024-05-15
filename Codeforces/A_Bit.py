n=int(input())
count=0
for i in range(n):
    str=input()
    if str[:2]=='++' or str[1:]=='++':
        count+=1
    else:
        count-=1
print(count)