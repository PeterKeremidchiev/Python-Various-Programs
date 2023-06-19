key = input()

command = input()

while command != "Generate":
    action = command.split(">>>")
    instruction = action[0]

    if instruction == "Contains":
        substr = action[1]
        if substr in key:
            print(f"{key} contains {substr}")
        else:
            print("Substring not found!")

    elif instruction == "Flip":
        upper_or_lower = action[1]
        start_idx = int(action[2])
        end_idx = int(action[3])
        if upper_or_lower == "Upper":
            key = key[:start_idx] + key[start_idx:end_idx].upper() + key[end_idx:]
            print(key)
        else:
            key = key[:start_idx] + key[start_idx:end_idx].lower() + key[end_idx:]
            print(key)
    elif instruction == "Slice":
        start_idx = int(action[1])
        end_idx = int(action[2])
        key = key[:start_idx] + key[end_idx:]
        print(key)

    command = input()

print(f"Your activation key is: {key}")
