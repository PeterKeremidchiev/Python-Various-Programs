SIZE = int(input())

sea_matrix = []
submarine_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    current_row = list(input())
    for col in current_row:
        if col == "S":
            submarine_pos = [row, current_row.index("S")]
            break
    sea_matrix.append(current_row)

mine_hits = 0
cruises_down = 0

while True:
    command = input()
    if mine_hits == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_pos[0]}, {submarine_pos[1]}]!")
        break
    if cruises_down == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    new_row = submarine_pos[0] + directions[command][0]
    new_col = submarine_pos[1] + directions[command][1]

    if sea_matrix[new_row][new_col] == "-":
        sea_matrix[submarine_pos[0]][submarine_pos[1]] = "-"
        submarine_pos = [new_row, new_col]
        sea_matrix[new_row][new_col] = "S"

    elif sea_matrix[new_row][new_col] == "*":
        mine_hits += 1
        sea_matrix[submarine_pos[0]][submarine_pos[1]] = "-"
        sea_matrix[new_row][new_col] = "S"
        submarine_pos = [new_row, new_col]

    elif sea_matrix[new_row][new_col] == "C":
        cruises_down += 1
        sea_matrix[submarine_pos[0]][submarine_pos[1]] = "-"
        submarine_pos = [new_row, new_col]
        sea_matrix[new_row][new_col] = "S"

for row in sea_matrix:
    print(''.join(row))




