n=int(input())
l_n=len(str(n))
i=n+1
while True:
    if len(set(str(i)))==l_n:
        break
    else:
        i+=1
print(i)