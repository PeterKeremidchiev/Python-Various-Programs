from collections import deque

caffeine = deque([int(x) for x in input().split(", ")])
drinks = deque([int(x) for x in input().split(", ")])

total_caffeine = 0
needed_caffeine = 300

while caffeine and drinks:
    caffe = caffeine.pop()
    drink = drinks.popleft()
    multiply = caffe * drink

    if multiply + total_caffeine <= 300:
        total_caffeine += multiply
    elif multiply + total_caffeine > 300:
        drinks.append(drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if drinks:
    print(f"Drinks left: {', '.join(str(x) for x in drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
