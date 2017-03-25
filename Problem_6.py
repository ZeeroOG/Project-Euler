def sum_of_square(n):
	result = 0
	for i in range(1, n+1):
		result += i**2
	return result

def sum_squared(n):
	result = 0
	for i in range(1, n+1):
		result += i
	return result**2

n = 100
print(sum_squared(n)-sum_of_square(n))
