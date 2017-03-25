rng = 4000000
rep = 0

fib1 = 1
fib2 = 0

while 1:
	temp = fib1
	fib1 += fib2
	fib2 = temp
	if (fib1 < rng):
		if (fib1 % 2 == 0):
			rep += fib1
	else:
		print(rep)
		break
