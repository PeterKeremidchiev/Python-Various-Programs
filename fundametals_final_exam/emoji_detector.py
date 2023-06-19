import re

text = input()

pattern = r"(::|\*\*)(?P<emojis>[A-Z][a-z]{2,})(\1)"

emojis = re.finditer(pattern, text)
digits = re.findall(r"\d", text)
final_digits = [int(x) for x in digits]
cool_treshold = 1

for d in final_digits:
    cool_treshold *= d
print(f"Cool threshold: {cool_treshold}")

emojis_found = 0
emos_to_print = []

for emo in emojis:
    emojis_found += 1
    emos = emo.groupdict()
    count_ascii = 0

    for letter in emos["emojis"]:
        count_ascii += ord(letter)
    if count_ascii >= cool_treshold:
        emo_for_list = emo.group(1) + emos["emojis"] + emo.group(1)
        emos_to_print.append(emo_for_list)

print(f"{emojis_found} emojis found in the text. The cool ones are:")
for emos in emos_to_print:
    print(emos)

