from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque(input().split())
total_honey = 0

opertions = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

while bees and nectar:
    bee = bees.popleft()
    nect = nectar.pop()

    if nect < bee:
        bees.appendleft(bee)

    elif nect >= bee:
        total_honey += abs(opertions[symbols.popleft()](bee, nect))
        # symbol = symbols.popleft()
        # if symbol == "+":
        #     total_honey += abs(bee + nect)
        # elif symbol == "-":
        #     total_honey += abs(bee - nect)
        # elif symbol == "*":
        #     total_honey += abs(bee * nect)
        # elif symbol == "/":
        #     if nect == 0:
        #         continue
        #     total_honey += abs(bee / nect)



print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
