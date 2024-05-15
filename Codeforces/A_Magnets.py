n=int(input())
cnt=0
prev=input()
for i in range(1,n):
    cur=input()
    if cur!=prev:
        prev=cur
        cnt+=1
print(cnt+1)