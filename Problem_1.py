rng = 1000
rep = 0

for x in range(1, rng):
	if (x % 3 == 0 or x % 5 == 0):
		rep += x

print (rep)
