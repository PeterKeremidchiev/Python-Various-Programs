from collections import deque

def check_for_empty(textile, meds):
    if not any([textile, meds]):
        return f"Textiles and medicaments are both empty."

    if not textile:
        return f"Textiles are empty."

    if not meds:
        return f"Medicaments are empty."


textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

healings = {
    "Patch": [30, 0],
    "Bandage": [40, 0],
    "MedKit": [100, 0],
}

while textiles and medicaments:
    curr_textile = textiles.popleft()
    curr_medicament = medicaments.pop()

    sum_of_products = curr_textile + curr_medicament

    if sum_of_products > 100:
        healings["MedKit"][1] += 1
        remaining = sum_of_products - 100
        medicaments[-1] += remaining
        continue

    for key, value in healings.items():
        if sum_of_products == value[0]:
            healings[key][1] += 1
            break
    else:
        medicaments.append(curr_medicament + 10)
new_dict = {}
for key, value in healings.items():
    if value[1]:
        new_dict[key] = value[1]

print(check_for_empty(textiles, medicaments))
if new_dict:
    sorted_dict = sorted(new_dict.items(), key=lambda x: (-x[1], x[0]))
    print('\n'.join([f"{key} - {value}" for key, value in sorted_dict if value != 0]))

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")



