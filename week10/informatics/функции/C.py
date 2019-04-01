def xor(x, y):
    if((x == 1 and y != 1) or (y == 1 and x != 1)):
    	return 1
    else:
    	return 0


s = input()
a = int(s[0])
b = int(s[2])

print(xor(a, b))