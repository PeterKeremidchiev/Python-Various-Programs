SIZE = int(input())

commands = input().split(", ")

matrix = []
squirel_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    current_row = list(input())
    for col in current_row:
        if col == "s":
            squirel_pos = [row, current_row.index("s")]
            break
    matrix.append(current_row)

out_of_matrix = False
trap = False
hazelnuts_done = False
count_hazelnuts = 0

for command in commands:
    if count_hazelnuts == 3:
        # hazelnuts_done = True
        break
    new_row = squirel_pos[0] + directions[command][0]
    new_col = squirel_pos[1] + directions[command][1]
    if not (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0])):
        out_of_matrix = True
        break
    if matrix[new_row][new_col] == "h":
        count_hazelnuts += 1
        matrix[squirel_pos[0]][squirel_pos[1]] = "*"
        squirel_pos = [new_row, new_col]
    elif matrix[new_row][new_col] == "*":
        matrix[squirel_pos[0]][squirel_pos[1]] = "*"
        squirel_pos = [new_row, new_col]

    elif matrix[new_row][new_col] == "t":
        trap = True
        break

if count_hazelnuts == 3:
    print("Good job! You have collected all hazelnuts!")
    print(f"Hazelnuts collected: {count_hazelnuts}")
if trap:
    print("Unfortunately, the squirrel stepped on a trap...")
    print(f"Hazelnuts collected: {count_hazelnuts}")
if out_of_matrix:
    print("The squirrel is out of the field.")
    print(f"Hazelnuts collected: {count_hazelnuts}")
if not any([trap, out_of_matrix]) and count_hazelnuts < 3:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {count_hazelnuts}")
