rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
command = input()

while command != "END":
    action = command.split()
    if len(action) == 5 and action[0] == "swap":
        row_1 = int(action[1])
        col_1 = int(action[2])
        row_2 = int(action[3])
        col_2 = int(action[4])
        if 0 <= row_1 <= rows and 0 <= row_2 <= rows and 0 <= col_1 <= columns and 0 <= col_2 <= columns:
            matrix[row_1][col_1] = matrix[row_2][col_2]
            print(*matrix, sep="\n")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()