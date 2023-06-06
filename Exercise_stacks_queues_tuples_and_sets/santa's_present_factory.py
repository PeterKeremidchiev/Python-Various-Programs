from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())
crafted = []

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    product = material * magic_level
    if product == 150:
        crafted.append("Doll")
        continue
    elif product == 250:
        crafted.append("Wooden train")
        continue
    elif product == 300:
        crafted.append("Teddy bear")
        continue
    elif product == 400:
        crafted.append("Bicycle")
        continue
    if product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]