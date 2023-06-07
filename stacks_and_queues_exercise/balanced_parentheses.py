from collections import deque

parenthesis = deque(input())
open_parent = deque()
flag = False

while parenthesis:
    current = parenthesis.popleft()

    if current in "({[":
        open_parent.append(current)
    elif not open_parent:
        flag = True
        break
    else:
        if f'{open_parent.pop() + current}' not in "(){}[]":
            flag = True
            break
if flag:
    print("NO")
else:
    print("YES")

