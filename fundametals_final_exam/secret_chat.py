concealed = input()

command = input()

while command != "Reveal":
    line = command.split(":|:")
    action = line[0]

    if action == "InsertSpace":
        index = int(line[1])
        concealed = concealed[:index] + " " + concealed[index:]
        print(concealed)

    elif action == "Reverse":
        substr = line[1]
        if substr in concealed:
            concealed = concealed.replace(substr, "", 1)
            reversed = substr[::-1]
            concealed = concealed + reversed
            print(concealed)
        else:
            print("error")

    elif action == "ChangeAll":
        substr = line[1]
        replacement = line[2]
        concealed = concealed.replace(substr, replacement)
        print(concealed)

    command = input()
print(f"You have a new text message: {concealed}")