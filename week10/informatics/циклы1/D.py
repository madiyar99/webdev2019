a = int( input())

i = 2

while i <= 30000:
	if(a % i == 0):
		print(i)
		break
	i = i + 1