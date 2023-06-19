import re

text = input()

pattern = r"([||#])(?P<item>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"

result = re.finditer(pattern, text)
total_calories = 0
result_2 = re.finditer(pattern, text)

for item in result:
    dict = item.groupdict()
    total_calories += int(dict["calories"])

days_left = total_calories // 2000
print(f"You have food to last you for: {days_left} days!")

for it in result_2:
    data = it.groupdict()
    print(f"Item: {data['item']}, Best before: {data['date']}, Nutrition: {data['calories']}")


