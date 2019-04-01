i=int(input())
print(len(list(i for i in map(int, input().split()) if i > 0)))