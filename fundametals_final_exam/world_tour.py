initial = input()

command = input()

while command != "Travel":
    line = command.split(":")
    action = line[0]

    if action == "Add Stop":
        index = int(line[1])
        string = line[2]
        if 0 <= index < len(initial):
            initial = initial[:index] + string + initial[index:]
            print(initial)
        else:
            print(initial)

    if action == "Remove Stop":
        start_index = int(line[1])
        end_index = int(line[2])
        if 0 <= start_index < len(initial) and 0 <= end_index < len(initial):
            initial = initial[:start_index] + initial[end_index + 1:]
            print(initial)
        else:
            print(initial)

    if action == "Switch":
        old_string = line[1]
        new_string = line[2]
        if old_string in initial:
            initial = initial.replace(old_string, new_string)
            print(initial)
        else:
            print(initial)
    command = input()

print(f"Ready for world tour! Planned stops: {initial}")