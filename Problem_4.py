from math import *

def palindrome(num):
    s = str(num)
    s1, s2 = s[:floor(len(s)/2)], s[ceil(len(s)/2):]
    return s1 == s2[::-1]

results = []
a = 100
b = 1000

for x in range(a, b):
    for y in range(a, b):
        if palindrome(x * y):
            results.append(x * y)

results = sorted(results)
for result in results:
    print(result)
