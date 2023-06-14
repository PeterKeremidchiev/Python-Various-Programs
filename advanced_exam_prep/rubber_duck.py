from collections import deque

time = deque([int(x) for x in input().split()])
number_of_tasks = deque([int(x) for x in input().split()])

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while time:
    programer_time = time.popleft()
    number = number_of_tasks.pop()
    multiply = programer_time * number

    if 0 <= multiply <= 60:
        ducks["Darth Vader Ducky"] += 1
    elif 60 < multiply <= 120:
        ducks["Thor Ducky"] += 1
    elif 120 < multiply <= 180:
        ducks["Big Blue Rubber Ducky"] += 1
    elif 180 < multiply <= 240:
        ducks["Small Yellow Rubber Ducky"] += 1
    else:
        number -= 2
        time.append(programer_time)
        number_of_tasks.append(number)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print('\n'.join([f"{key}: {value}" for key, value in ducks.items()]))