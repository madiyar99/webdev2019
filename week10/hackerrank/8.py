n = int(input())

arr = []


for i in range(n):
	lis = [1, "madiyar"]
	lis[0] = input()
	lis[1] = float(input())
	arr.append(lis)

arr.sort()

maxi1 = 100000000
maxi2 = 100000000

for i in range(n):
	if(arr[i][1] < maxi1):
		maxi1 = arr[i][1]

for i in range(n):
	if(arr[i][1] < maxi2 and arr[i][1] != maxi1):
		maxi2 = arr[i][1]

if(maxi2 == 100000000):
	maxi2 = maxi1

for i in range(n):
	if(arr[i][1] == maxi2):
		print(arr[i][0])


