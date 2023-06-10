rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]
count_same = 0

for i in range(rows - 1):
    for j in range(columns - 1):
        curr_el = matrix[i][j]
        below_el = matrix[i + 1][j]
        next_el = matrix[i][j + 1]
        diag = matrix[i + 1][j + 1]
        if curr_el == below_el == next_el == diag:
            count_same += 1
print(count_same)
