n = int(input())
cars = {}

for i in range(n):
    car = input().split("|")
    model = car[0]
    mileage = int(car[1])
    fuel = int(car[2])
    cars[model] = {"mileage": mileage, "fuel": fuel}

command = input()

while command != "Stop":
    line = command.split(" : ")
    action = line[0]

    if action == "Drive":
        car = line[1]
        distance = int(line[2])
        fuel = int(line[3])
        if fuel > cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] > 100000:
                del cars[car]
                print(f"Time to sell the {car}!")
    elif action == "Refuel":
        car = line[1]
        fuel = int(line[2])
        if cars[car]["fuel"] > 75:
            continue
        else:
            diff = abs(75 - cars[car]["fuel"])
            cars[car]["fuel"] += fuel

            if cars[car]["fuel"] > 75:
                cars[car]["fuel"] = 75

            if fuel > diff:
                print(f'{car} refueled with {diff} liters')
            else:
                print(f'{car} refueled with {fuel} liters')

    elif action == "Revert":
        car = line[1]
        kilometers = int(line[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for key, value in cars.items():
    print(f"{key} -> Mileage: {cars[key]['mileage']} kms, Fuel in the tank: {cars[key]['fuel']} lt.")