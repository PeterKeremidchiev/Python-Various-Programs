SIZE = 8

board = []
white_pawn_cordinates = []
black_pawn_cordinates = []

for row in range(SIZE):
    current_row = input().split()
    for col in current_row:
        if col == "b":
            black_pawn_cordinates = [row, current_row.index("b")]
        if col == "w":
            white_pawn_cordinates = [row, current_row.index("w")]
    board.append(current_row)

if abs(white_pawn_cordinates[1] - black_pawn_cordinates[1]) != 1 or black_pawn_cordinates[0] > white_pawn_cordinates[0]:
    if abs(SIZE - white_pawn_cordinates[0] - 1) <= black_pawn_cordinates[0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_pawn_cordinates[1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_pawn_cordinates[1])}8.")
else:
    place = (black_pawn_cordinates[0] + white_pawn_cordinates[0]) // 2

    if black_pawn_cordinates[0] % 2 == white_pawn_cordinates[0] % 2:
        print(f"Game over! Black win, capture on {chr(97 + white_pawn_cordinates[1])}{SIZE - place}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + black_pawn_cordinates[1])}{SIZE - place}.")