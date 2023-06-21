password = input()

command = input()

while command != "Done":
    action = command.split(" ")
    event = action[0]
    if event == "TakeOdd":
        password = password[1::2]
        print(password)

    elif event == "Cut":
        idx = int(action[1])
        lenght = int(action[2])
        password = password[:idx] + password[idx + lenght:]
        print(password)

    elif event == "Substitute":
        substring = action[1]
        substitude = action[2]
        if substring in password:
            password = password.replace(substring, substitude)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()
print(f"Your password is: {password}")



