rows, columns = [int(x) for x in input().split()]

start = ord("a")

for row in range(start, start + rows):
    for col in range(start, start + columns):
        print(f"{chr(row)}{chr(row + col - start)}{chr(row)}", end=" ")
    print()