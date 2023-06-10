rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]

primary = [matrix[idx][idx] for idx in range(rows)]
secondary = [matrix[idx][rows - idx - 1] for idx in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")
