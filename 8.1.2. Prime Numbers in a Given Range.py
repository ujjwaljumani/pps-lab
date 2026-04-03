start = int(input())
end = int(input())

def is_prime(num):
	if num < 2:
		return False
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True

found_prime = False
for n in range(start, end + 1):
	if is_prime(n):
		print(n)
		found_prime = True

if not found_prime:
	print("No primes")
