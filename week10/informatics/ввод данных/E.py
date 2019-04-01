v = int (input())

t = int (input())

s = v * t

if s > 109:
	s = s % 109

elif s < 109:
	s = (109 + ((v * t) % 109)) % 109

print(s)

