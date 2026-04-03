text = input()
result = ""
for char in text:
	if char.isalnum() or char.isspace():
		result += char
print(result)
