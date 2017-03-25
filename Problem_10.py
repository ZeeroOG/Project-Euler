def is_prime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

result = 0
limit = 2000000

for i in range(2, limit):
	if is_prime(i):
		result += i

print(result)
