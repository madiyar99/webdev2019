import math
a = int( input())
b = int( input())

y = 1;
y2 = 1.15;

while a <= b:
	y2 = math.sqrt(a)
	if(a % y2 == 0):
		print(a)
	a = a + 1