import random

dice_1 = random.randint(1, 7)
dice_2 = random.randint(1, 7)
sum = dice_1 + dice_2

question = int(input("What is the total (2-12)? "))

while int(question) != sum:
    print(f"What is the total (2-12)? {question}")
    question = input("What is the total (2-12)? ")

print("You got it!")