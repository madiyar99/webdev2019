x=int(input())
a = ([int(x) for x in input().split()])
a2 = a[::2]
print(*a2)