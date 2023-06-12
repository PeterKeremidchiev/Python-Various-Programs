rows, cols = [int(x) for x in input().split()]

player_pos = []
playground = [[x for x in input().split()] for i in range(rows)]

player_found = False
for row in range(rows):
    for col in range(cols):
        if playground[row][col] == "B":
            player_pos = [row, col]
            # playground[row][col] = "-"
            player_found = True
            break
    if player_found:
        break


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

count_opponents_destroyed = 0
moves_counter = 0

command = input()

while command != "Finish":
    new_row = player_pos[0] + directions[command][0]
    new_col = player_pos[1] + directions[command][1]
    if not (0 <= new_row < len(playground) and 0 <= new_col < len(playground[0])):
        command = input()
        continue

    if playground[new_row][new_col] == "P":
        count_opponents_destroyed += 1
        moves_counter += 1
        player_pos = [new_row, new_col]
        if count_opponents_destroyed == 3:
            break

    elif playground[new_row][new_col] == "-":
        playground[player_pos[0]][player_pos[1]] = "-"
        player_pos = [new_row, new_col]
        moves_counter += 1

    command = input()

print("Game over!")
print(f"Touched opponents: {count_opponents_destroyed} Moves made: {moves_counter}")

