stack = [int(x) for x in input().split()]

rack_cap = int(input())

racks = 1
current_rack_space = rack_cap

while stack:
    removed = stack.pop()

    if current_rack_space >= removed:
        current_rack_space -= removed

    else:
        racks += 1
        current_rack_space = rack_cap - removed

print(racks)
