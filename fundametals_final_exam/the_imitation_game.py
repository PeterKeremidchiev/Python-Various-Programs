text = input()

command = input()

while command != "Decode":
    line = command.split("|")
    action = line[0]

    if action == "Move":
        text = text[int(line[1]):] + text[:int(line[1])]

    elif action == "Insert":
        index = int(line[1])
        chars = line[2]
        text = text[:index] + chars + text[index:]
        
    elif action == "ChangeAll":
        substring = line[1]
        replacement = line[2]
        text = text.replace(substring, replacement)

    command = input()
print(f"The decrypted message is: {text}")
