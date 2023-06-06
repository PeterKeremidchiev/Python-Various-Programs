from collections import deque

chocolate = deque([int(x) for x in input().split(", ")])
milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0


while len(chocolate) != 0 and len(milk) != 0 and milkshakes != 5:
    last_choco = chocolate.pop()
    first_milk = milk.popleft()
    if last_choco <= 0 and first_milk <=0:
        continue
    if last_choco <= 0:
        milk.appendleft(first_milk)
        continue
    if first_milk <= 0:
        chocolate.append(last_choco)
        continue
    if last_choco == first_milk:
        milkshakes += 1
    else:
        milk.append(first_milk)
        chocolate.append(last_choco - 5)


if milkshakes >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f'Chocolate: {", ".join(str(x) for x in chocolate) or "empty"}')
print(f"Milk: {', '.join(str(x) for x in milk) or 'empty'}")

