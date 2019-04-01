x=int(input())
print(*[int(x) for x in input().split() if not int(x)%2])