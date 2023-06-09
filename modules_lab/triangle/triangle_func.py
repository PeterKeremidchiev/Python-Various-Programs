def upper_triangle(n):
    for row in range(1, n + 2):
        for j in range(1, row):
            print(j, end=" ")
        print()

def lower_triangle(n):
    for row in range(n, 0, -1):
        for i in range(1, row):
            print(i, end=" ")
        print()

def triangle(n):
    upper_triangle(n)
    lower_triangle(n)

