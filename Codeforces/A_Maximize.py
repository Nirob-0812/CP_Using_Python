import math
 
t=int(input())
for i in range(t):
    x=int(input())
    max=0
    max_y=1
    for y in range(x-1,0,-1):
        res=math.gcd(x,y)+y
        if max<res:
            max=res
            max_y=y
    
    print(max_y)