SIZE = 6

matrix = [input().split(" ") for x in range(SIZE)]

throws = 0
total_sum = 0
last_bucket = []

while True:
    if throws == 3:
        break
    current_sum = 0
    hit = input().split(", ")
    row = int(hit[0][1:])
    col = int(hit[1][0:-1])

    throws += 1
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        if matrix[row][col] == "B" and [row, col] not in last_bucket:
            last_bucket.append([row, col])
            for rows in matrix:
                if rows[col] == "B":
                    for cols in matrix:
                        if cols[col].isdigit():
                            total_sum += (int(cols[col]))

    # total_sum += current_sum

if total_sum < 100:
    print(f"Sorry! You need {100 - total_sum} points more to win a prize.")
elif 100 <= total_sum <= 199:
    print(f"Good job! You scored {total_sum} points, and you've won Football.")
elif 200 <= total_sum <= 299:
    print(f"Good job! You scored {total_sum} points, and you've won Teddy Bear.")
elif total_sum >= 300:
    print(f"Good job! You scored {total_sum} points, and you've won Lego Construction Set.")




