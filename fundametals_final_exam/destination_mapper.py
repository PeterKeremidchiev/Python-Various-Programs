import re

text = input()

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

destinations = re.finditer(pattern, text)
final_dest = []

for destination in destinations:
    final = destination.group(2)
    final_dest.append(final)

travel_points = 0

for i in final_dest:
    for j in i:
        travel_points += 1

print(f"Destinations: {', '.join(final_dest)}")
print(f"Travel Points: {travel_points}")


