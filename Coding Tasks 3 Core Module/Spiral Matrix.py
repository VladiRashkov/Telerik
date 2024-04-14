n = int(input())

matrix = [[0] * n for _ in range(n)]

current_number = 1
target_number = n * n
top_border = 0
bottom_border = n - 1
left_border = 0
right_border = n - 1

while current_number <= target_number:
    for i in range(left_border, right_border + 1):
        matrix[top_border][i] = current_number
        current_number += 1
    top_border += 1

    for j in range(top_border, bottom_border + 1):
        matrix[j][right_border] = current_number
        current_number += 1
    right_border -= 1

    for k in range(right_border, left_border - 1, -1):
        matrix[bottom_border][k] = current_number
        current_number += 1
    bottom_border -= 1

    for m in range(bottom_border, top_border - 1, -1):
        matrix[m][left_border] = current_number
        current_number += 1
    left_border += 1

for row in matrix:
    for col in row:
        print(f"{col}", end=" ")
    print()
