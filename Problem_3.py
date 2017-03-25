num = 600851475143

def is_prime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

if is_prime(num):
	print(num)
else:
	for i in range(2, num +1 ):
		if num % i == 0 and is_prime(i):
			print(i)

print("END")
