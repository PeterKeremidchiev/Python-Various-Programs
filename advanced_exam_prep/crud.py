SIZE = 6

matrix = [input().split(" ") for x in range(SIZE)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

first_pos = input().split(", ")
new_first_pos = []
for tupl in first_pos:
    for num in tupl:
        if num.isdigit():
            new_first_pos.append(int(num))


commands = input()
while commands != "Stop":
    line = commands.split(", ")
    action = line[0]
    direction = line[1]
    new_row = new_first_pos[0] + directions[direction][0]
    new_col = new_first_pos[1] + directions[direction][1]

    if action == "Create":
        string = line[2]
        if matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = string
            new_first_pos = [new_row, new_col]
        else:
            new_first_pos = [new_row, new_col]

    elif action == "Update":
        string = line[2]
        if not matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = string
            new_first_pos = [new_row, new_col]
        else:
            new_first_pos = [new_row, new_col]

    elif action == "Delete":
        if not matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = "."
            new_first_pos = [new_row, new_col]
        else:
            new_first_pos = [new_row, new_col]

    elif action == "Read":
        if not matrix[new_row][new_col] == ".":
            print(matrix[new_row][new_col])
            new_first_pos = [new_row, new_col]
        else:
            new_first_pos = [new_row, new_col]

    commands = input()
for row in matrix:
    print(" ".join(row))