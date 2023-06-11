SIZE = 6

deposits = {"W": ["Water", 0], "M": ["Metal", 0], "C": ["Concrete", 0]}

mars = []
rover_pos = []

directions = {
    "up": lambda r, c: [(r - 1) % SIZE, c],
    "down": lambda r, c: [(r + 1) % SIZE, c],
    "left": lambda r, c: [r, (c - 1) % SIZE],
    "right": lambda r, c: [r, (c + 1) % SIZE],
}

for row in range(SIZE):
    current_row = input().split()

    if "E" in current_row:
        rover_pos = [row, current_row.index("E")]

    mars.append(current_row)

commands = input().split(", ")

for command in commands:
    rover_pos = directions[command](rover_pos[0], rover_pos[1])
    position = mars[rover_pos[0]][rover_pos[1]]

    if position in deposits:
        deposits[position][1] += 1
        print(f"{deposits[position][0]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        # mars[position] = " - "
    elif position == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break
if all([value[1] for value in deposits.values()]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
