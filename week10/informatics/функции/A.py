a,b,c,d = map(int, input().split())


def _min(mass=[a, b, c, d]):
    min = mass[0]
    i = 0
    while i < len(mass):
        if min > mass[i]:
            min = mass[i]
        else:
            i += 1
    print(min)
_min()