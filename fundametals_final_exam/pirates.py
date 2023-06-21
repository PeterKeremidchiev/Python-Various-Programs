cities = {}

command = input()

while command != "Sail":
    line = command.split("||")
    city = line[0]
    population = int(line[1])
    gold = int(line[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    command = input()

while True:
    line = input()
    if line == "End":
        break
    action = line.split("=>")
    event = action[0]
    if event == "Plunder":
        town = action[1]
        people = int(action[2])
        gold = int(action[3])
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif event == "Prosper":
        town = action[1]
        gold = int(action[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for key, value in cities.items():
        print(f'{key} -> Population: {cities[key]["population"]} citizens, Gold: {cities[key]["gold"]} kg')
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")


