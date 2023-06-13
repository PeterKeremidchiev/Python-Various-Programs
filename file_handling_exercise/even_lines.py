import os

file_name = "text.txt"
abs_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(abs_path, file_name)


symbols = ["-", ",", ".", "!", "?"]

with open(file_path, "r") as file:
    content = file.readlines()

for r in range(0, len(content), 2):
    for sym in symbols:
        content[r] = content[r].replace(sym, "@")

    print(*content[r].split()[::-1], sep=" ")

