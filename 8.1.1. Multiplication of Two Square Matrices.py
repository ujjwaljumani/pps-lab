n = int(input("dimension: "))
print("first matrix:")
matrix1 = []
for _ in range(n):
	row = list(map(int, input().split()))
	matrix1.append(row)
print("second matrix:")
matrix2 = []
for _ in range(n):
	row = list(map(int, input().split()))
	matrix2.append(row)
result = [[0]*n for _ in range(n)]
for i in range(n):
	for j in range(n):
		for k in range(n):
			result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Resultant Matrix:")
for row in result:
	print(" ".join(map(str, row)))
