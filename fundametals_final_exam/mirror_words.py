import re

text = input()

pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matches = re.finditer(pattern, text)
count_words = 0
mirror_words = []

for match in matches:
    count_words += 1
    second = match.group(3)

    if match.group(2) == second[::-1]:
        mirror_words.append(match[2] + " <=> " + match[3])

if count_words == 0:
    print("No word pairs found!")
else:
    print(f"{count_words} word pairs found!")
# pairs = {}
if mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")

