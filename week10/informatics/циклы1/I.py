a = int( input())

i = 2
count = 2

while i < a:
	if a % i == 0:
		count = count + 1
	i = i + 1

print(count)