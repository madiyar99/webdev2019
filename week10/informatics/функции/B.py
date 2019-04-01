def power(a, n):
    p = 1
    for i in range(n):
        p = p * a
    return p


a, n = map(int, input().split())
print(int(power(a, n)))