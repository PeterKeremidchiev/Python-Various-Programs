rows, cols = [int(x) for x in input().split(",")]

cupboard = []

for i in range(rows):
    current_row = list(input())
    cupboard.append(current_row)

mouse_pos = []
cheese_positions = []

for row in range(rows):
    for col in range(cols):
        if cupboard[row][col] == "M":
            mouse_pos = [row, col]
        elif cupboard[row][col] == "C":
            cheese_positions.append([row, col])

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()
trap = False
no_more_cheese = False

while command != "danger":
    new_row = mouse_pos[0] + directions[command][0]
    new_col = mouse_pos[1] + directions[command][1]

    if not cheese_positions:
        print("Happy mouse! All the cheese is eaten, good night!")
        break

    if not (0 <= new_row < len(cupboard) and 0 <= new_col < len(cupboard[0])):
        print("No more cheese for tonight!")
        no_more_cheese = True
        break

    if cupboard[new_row][new_col] == "C":
        cheese_positions.remove([new_row, new_col])
        cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
        cupboard[new_row][new_col] = "M"
        mouse_pos = [new_row, new_col]

    elif cupboard[new_row][new_col] == "T":
        cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
        cupboard[new_row][new_col] = "M"
        print("Mouse is trapped!")
        trap = True
        break

    elif cupboard[new_row][new_col] == "*":
        cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
        cupboard[new_row][new_col] = "M"
        mouse_pos = [new_row, new_col]

    command = input()

if cheese_positions and not trap and not no_more_cheese:
    print("Mouse will come back later!")

for row in cupboard:
    print("".join(row))



