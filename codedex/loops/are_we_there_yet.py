answer = input("Are we there yet? ")
while answer != "Yes":
    question = f"Are we there yet? {answer}"
    print(question)
    answer = input()

question = f"Are we there yet? {answer}"
print(question)