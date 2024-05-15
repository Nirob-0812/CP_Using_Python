s=input()
numbers=s.split('+')
numbers=[*sorted(list(int(i) for i in numbers))]
s='+'.join([str(i) for i in numbers])
print(s)