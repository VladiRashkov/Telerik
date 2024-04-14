import sys

dimensions = input().split()

total_rows = int(dimensions[0])
total_cols = int(dimensions[1])

matrix = [[2**(row + col) for col in range(total_cols)] for row in range(total_rows)]

current_row = 0
current_col = 0

row_direction = 1
col_direction = 1

total_sum = matrix[current_row][current_col]

if total_rows == 1 or total_cols == 1:
    print(total_sum)
    sys.exit()


is_corner_hit = False

while not is_corner_hit:
    potential_next_row = current_row + row_direction
    potential_next_col = current_col + col_direction

    if potential_next_row < 0:
        row_direction = 1

    if potential_next_row >= total_rows:
        row_direction = -1

    if potential_next_col < 0:
        col_direction = 1

    if potential_next_col >= total_cols:
        col_direction = -1

    current_row += row_direction
    current_col += col_direction

    total_sum += matrix[current_row][current_col]

    if (current_row == 0 and current_col == 0) or (current_row == 0 and current_col == total_cols - 1) or \
       (current_row == total_rows - 1 and current_col == 0) or (current_row == total_rows - 1 and current_col == total_cols - 1):
        is_corner_hit = True

print(total_sum)
