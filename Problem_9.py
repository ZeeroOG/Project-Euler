limit = 1000

for a in range(1, limit+1):
	for b in range(a, limit+1):
		c = (a**2 + b**2)**0.5
		if a + b + c == limit:
			print("a => " + str(a))
			print("b => " + str(b))
			print("c => " + str(c))
			print("result => " + str(a*b*c))
			break
