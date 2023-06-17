from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])
challenges = deque([int(x) for x in input().split()])


while tools and substances and challenges:

    tool = tools.popleft()
    subs = substances.pop()
    multiply = tool * subs

    if multiply in challenges:
        challenges.remove(multiply)

    elif multiply not in challenges:
        tool += 1
        tools.append(tool)
        if subs > 1:
            subs -= 1
            substances.append(subs)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")

