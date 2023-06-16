def forecast(*args):

    sunny_locations = []
    cloudy_locations = []
    rainy_locations = []

    for arg in args:
        if arg[1] == "Sunny":
            sunny_locations.append(arg[0])
        elif arg[1] == "Cloudy":
            cloudy_locations.append(arg[0])
        elif arg[1] == "Rainy":
            rainy_locations.append(arg[0])
    sunny_locations.sort()
    cloudy_locations.sort()
    rainy_locations.sort()
    result = []

    if sunny_locations:
        for loc in sunny_locations:
            result.append(f"{loc} - Sunny")
    if cloudy_locations:
        for loc in cloudy_locations:
            result.append(f"{loc} - Cloudy")
    if rainy_locations:
        for loc in rainy_locations:
            result.append(f"{loc} - Rainy")
    return "\n".join(result)







print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


