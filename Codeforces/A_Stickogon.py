t=int(input())
for i in range(t):
    n=int(input())
    arr=[0]*101
    res=0
    values=map(int,input().split())
    for j in values:
        arr[j]+=1

    for index,value in enumerate(arr):
        if value>2:
            c=value//3
            res+=c
    print(res)


    