from collections import deque

elves = deque([int(x) for x in input().split()])
energy = deque([int(x) for x in input().split()])
count_elve = 0
toys = 0
total_energy = 0

while elves and energy:
    elf = elves.popleft()
    curr_energy = energy[-1]

    if elf < 5:

        continue
    current_toys = 0
    count_elve += 1

    if count_elve % 3 == 0:
        curr_energy *= 2
        current_toys += 1

    if elf >= curr_energy:
        total_energy += curr_energy
        elf -= curr_energy

        if count_elve % 5 != 0:
            elf += 1
            current_toys += 1
        else:
            current_toys = 0
        energy.pop()
    else:
        elf *= 2
        current_toys = 0

    toys += current_toys
    elves.append(elf)

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")
if elves:
    print(f'Elves left: {", ".join(str(x) for x in elves)}')
if energy:
    print(f'Boxes left: {", ".join(str(x) for x in energy)}')





