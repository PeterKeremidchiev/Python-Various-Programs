
SIZE = 6
player_names = input().split(", ")

maze = [input().split(" ") for x in range(SIZE)]
first_player_rest = False
second_player_rest = False

while True:
    first_player_cordinates = input().split(", ")
    if not first_player_rest:
        row = int(first_player_cordinates[0][1:])
        col = int(first_player_cordinates[1][0:-1])

        if maze[row][col] == "E":
            print(f"{player_names[0]} found the Exit and wins the game!")
            break
        elif maze[row][col] == "T":
            print(f"{player_names[0]} is out of the game! The winner is {player_names[1]}.")
            break
        elif maze[row][col] == "W":
            print(f"{player_names[0]} hits a wall and needs to rest.")
            first_player_rest = True
    else:
        first_player_rest = False

    second_player_cordinates = input().split(", ")
    if not second_player_rest:
        row = int(second_player_cordinates[0][1:])
        col = int(second_player_cordinates[1][0:-1])

        if maze[row][col] == "E":
            print(f"{player_names[1]} found the Exit and wins the game!")
            break
        elif maze[row][col] == "T":
            print(f"{player_names[1]} is out of the game! The winner is {player_names[0]}.")
            break
        elif maze[row][col] == "W":
            print(f"{player_names[1]} hits a wall and needs to rest.")
            second_player_rest = True
    else:
        second_player_rest = False


