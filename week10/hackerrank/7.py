n = int(input())

lis = list(map(int, input().split()))

maxi = max(lis)
maxi1 = -10000000

for i in range(n):
	if(lis[i] > maxi1 and lis[i] != maxi):
		maxi1 = lis[i]

print(maxi1)

