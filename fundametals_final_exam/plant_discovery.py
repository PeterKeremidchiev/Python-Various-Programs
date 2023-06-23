n = int(input())

plants = {}

for pl in range(n):
    line = input().split("<->")
    plant = line[0]
    rarity = line[1]
    if plant not in plants:
        plants[plant] = {"rarity": rarity, "rating": []}
    else:
        plants[plant]["rarity"] = rarity

command = input()

while command != "Exhibition":
    line = command.split(": ")
    action = line[0]
    line.pop(0)
    line_2 = "".join(line)
    line_3 = line_2.split(" - ")

    if action == "Rate":
        plant = line_3[0].strip()
        rating = float(line_3[1])
        if plant in plants:
            plants[plant]["rating"].append(rating)
        else:
            print("error")

    elif action == "Update":
        plant = line_3[0].strip()
        new_rarity = int(line_3[1])
        if plant in plants:
            plants[plant]["rarity"] = new_rarity
        else:
            print("error")

    elif action == "Reset":
        plant = line_3[0].strip()
        if plant in plants:
            plants[plant]["rating"] = []
        else:
            print("error")

    command = input()

final_ratings = 0
print("Plants for the exhibition:")
for key, value in plants.items():
    if len(value['rating']) == 0:
        final_ratings = 0
    else:
        final_ratings = sum(value['rating']) / len(value['rating'])
    print(f'- {key}; Rarity: {plants[key]["rarity"]}; Rating: {final_ratings:.2f}')


