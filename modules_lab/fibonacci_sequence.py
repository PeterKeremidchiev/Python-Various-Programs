from triangle.fibonacci import create_fibonacci_seq, locate_num

command = input()

while command != "Stop":
    action = command.split()
    if action[0] == "Create":
        sequence = create_fibonacci_seq(int(action[2]))
        print(*sequence, sep=" ")
    elif action[0] == "Locate":
        locate_num(int(action[1]), sequence)

    command = input()
