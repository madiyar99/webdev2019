arr = []

n = int(input())

for i in range(n):
	lis = list(input().split())
	if(lis[0] == "insert"):
		arr.insert(int(lis[1]), int(lis[2]))

	elif(lis[0] == "print"):	
		print(arr)

	elif(lis[0] == "remove"):
		arr.remove(int(lis[1]))

	elif(lis[0] == "append"):
		arr.append(int(lis[1]))

	elif(lis[0] == "sort"):
		arr.sort()

	elif(lis[0] == "pop"):
		arr.pop()

	elif(lis[0] == "reverse"):
		arr.reverse()
