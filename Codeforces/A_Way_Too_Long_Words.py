t=int(input())
for i in range(t):
    str=input()
    l=len(str)
    if l>10:
        print(f'{str[0]}{l-2}{str[-1]}')
    else:
        print(str)