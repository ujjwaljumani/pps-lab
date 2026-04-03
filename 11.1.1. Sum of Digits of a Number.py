num = int(input("Enter a number: "))
digit_sum = 0
temp = abs(num)
while temp > 0:
	digit_sum += temp % 10
	temp //= 10
print("Sum of digits:",digit_sum)
