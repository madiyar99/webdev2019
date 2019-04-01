a = int(input())
i = 0
sum1 = 1

while i >= 0:
	
	for j in range(i):
		sum1 = sum1 * 2

	if sum1 <= a:
		print(sum1)

	else:
		break

	i = i + 1
	sum1 = 1