rng = 20
num = rng

while 1:
	i = 0
	for x in range(1, rng+1):
		if(num % x == 0):
			i += 1
		else:
			break
	if(i == rng):
		print (num)
		break
	num += 1
