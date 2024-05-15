def min_new_problems(a, b):
    n = len(a)
    new_problems = 0

    for i in range(n):
        if a[i] > b[i]:
            a.append(b[i])
            a.sort() 
            a.pop() 
            new_problems += 1

    return new_problems

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split())) 

    print(min_new_problems(a, b))
