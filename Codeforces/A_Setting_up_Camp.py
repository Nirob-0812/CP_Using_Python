t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    tent=a
    if b%3!=0:
        need=3-b%3
        if c<need:
            print('-1')
        else:
            tent+=(b//3)+1
            c=c-need
            if c%3==0:
                tent+=c//3
            else:
                tent+=(c//3)+1
            print(tent)

    else:
        tent+=b//3
        if c%3==0:
            tent+=c//3
        else:
            tent+=(c//3)+1
        print(tent)

