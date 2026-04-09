def generate_fibonacci_sequence(max_value):
	sequence = []
	a, b = 0, 1
	while a <= max_value:
		sequence.append(a)
		a, b = b, a + b
	return sequence
