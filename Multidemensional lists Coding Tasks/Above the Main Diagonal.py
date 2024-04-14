n = int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(2 ** (j + i)) 
    matrix.append(row)
sum = 0
for k in range(n):
    for m in range(k + 1, n):
        sum += matrix[k][m]
print(sum)