arr = [3,0,1,1,9,7]; a = 7; b = 2; c = 3
triplet=max(a,b,)
n=len(arr)
cnt=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if((arr[i]-arr[j])<=a and (arr[j]-arr[k])<=b and (arr[i]-arr[k])<=c):
                cnt+=1

print(cnt)