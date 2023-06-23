n = int(input())
pieces = {}

for i in range(n):
    line = input().split("|")
    piece = line[0]
    composer = line[1]
    key = line[2]
    pieces[piece] = {"composer": composer, "key": key}

command = input()

while command != "Stop":
    line = command.split("|")
    action = line[0]

    if action == "Add":
        piece = line[1]
        composer = line[2]
        key = line[3]
        if piece not in pieces:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        piece = line[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = line[1]
        new_key = line[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
for key, value in pieces.items():
    print(f"{key} -> Composer: {pieces[key]['composer']}, Key: {pieces[key]['key']}")