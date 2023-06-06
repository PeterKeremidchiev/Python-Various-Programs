from collections import deque
from math import floor

numbers = deque(input().split())

idx = 0

while idx < len(numbers):
    element = numbers[idx]

    if element == "*":
        for _ in range(idx - 1):
            numbers.appendleft(int(numbers.popleft()) * int(numbers.popleft()))

    elif element == "/":
        for _ in range(idx - 1):
            numbers.appendleft(int(numbers.popleft()) / int(numbers.popleft()))

    elif element == "+":
        for _ in range(idx - 1):
            numbers.appendleft(int(numbers.popleft()) + int(numbers.popleft()))

    elif element == "-":
        for _ in range(idx - 1):
            numbers.appendleft(int(numbers.popleft()) - int(numbers.popleft()))

    if element in "*/+-":
        del numbers[1]
        idx = 1
    idx += 1

print(floor(int(numbers[0])))