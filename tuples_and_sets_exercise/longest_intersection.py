n = int(input())
longest_intersec = set()


for i in range(n):
    first_data, second_data = [el.split(",") for el in input().split("-")]
    # splited_first = [int(x) for x in first_data.split(",")]
    # splited_second = [int(x) for x in second_data.split(",")]
    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))
    intersect = first_range.intersection(second_range)
    if len(intersect) > len(longest_intersec):
        longest_intersec = intersect

print(f"Longest intersection is {list(longest_intersec)} with length {len(longest_intersec)}")


