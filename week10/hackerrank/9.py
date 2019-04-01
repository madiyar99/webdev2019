n = int(input())

arr = []

for i in range(n):
	lis = list(input().split())	
	arr.append(lis)

name = input()

for i in range(n):
	if(arr[i][0] == name):
		math = float(arr[i][1])
		physics = float(arr[i][2])
		chemistry = float(arr[i][3])
		average = float((math + physics + chemistry) / 3)
		break

print('{0:.2f}'.format(average))
