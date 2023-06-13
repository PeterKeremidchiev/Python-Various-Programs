import os

abs_path = os.path.dirname(os.path.abspath(__file__))

command = input()

while command != "End":
    action = command.split("-")
    file_name = action[1]
    if action[0] == "Create":
        file_path = os.path.join(abs_path, file_name)
        with open(file_path, "w"):
            pass

    elif action[0] == "Add":
        content = action[2]
        file_path = os.path.join(abs_path, file_name)
        with open(file_path, "a") as file:
            file.write(f"{content}\n")

    elif action[0] == "Replace":
        file_path = os.path.join(abs_path, file_name)
        old_string = action[2]
        new_string = action[3]
        try:
            with open(file_path, "r+") as file:
                content = file.read()
                content = content.replace(old_string, new_string)
                file.seek(0)
                file.write(content)
        except FileNotFoundError:
            print("An error occurred")

    elif action[0] == "Delete":
        file_path = os.path.join(abs_path, file_name)
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")
    command = input()

