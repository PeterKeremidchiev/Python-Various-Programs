rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
maximal_sum = float("-inf")
new_matrix = []

for i in range(rows - 2):
    for j in range(columns - 2):
        # curr_el = matrix[i][j]
        # below_el = matrix[i + 1][j]
        # below_below = matrix[i + 2][j]
        # next_el = matrix[i][j + 1]
        # diag = matrix[i + 1][j + 1]
        # next_diag = matrix[i + 2][j + 1]
        # third_el = matrix[i][j + 2]
        # third_below = matrix[i + 1][j + 2]
        # third_diag = matrix[i + 2][j + 2]
        first_row = matrix[i][j:j + 3]
        second_row = matrix[i + 1][j:j + 3]
        third_row = matrix[i + 2][j:j + 3]
        total_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if maximal_sum < total_sum:
            maximal_sum = total_sum
            new_matrix = [first_row, second_row, third_row]

print(f"Sum = {maximal_sum}")
print(*new_matrix[0])
print(*new_matrix[1])
print(*new_matrix[2])
