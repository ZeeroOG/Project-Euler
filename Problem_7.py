def is_prime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

n = 10001
count = 0

i = 1
while 1:
	i += 1
	if is_prime(i):
		count += 1
		print(str(count) + " => " + str(i))
		if count == n:
			break
