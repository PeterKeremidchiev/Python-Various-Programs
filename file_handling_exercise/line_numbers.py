import os

file_name = "text_2.txt"
abs_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(abs_path, file_name)

output_file_name = "output.txt"
output_file_path = os.path.join(abs_path, output_file_name)

symbols = ["-", ",", ".", "!", "?", "'"]

with open(file_path, "r") as file:
    content = file.readlines()

for row in range(len(content)):
    count_letters = 0
    count_punctuation = 0
    for letter in content[row]:
        if letter.isalnum():
            count_letters += 1
        elif letter in symbols:
            count_punctuation += 1
    with open(output_file_path, "a") as file:
        file.write(f"Line {row + 1}: {''.join(content[row][:-1])} ({count_letters})({count_punctuation})\n")

