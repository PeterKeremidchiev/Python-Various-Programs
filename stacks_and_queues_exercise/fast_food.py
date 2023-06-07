from collections import deque

quantity = int(input())

clients = deque([int(x) for x in input().split()])

print(max(clients))

for num in clients.copy():
    if quantity >= num:
        clients.popleft()
        quantity -= num

    else:
        print(f"Orders left: {' '.join([str(x) for x in clients])}")
        break
else:
    print("Orders complete")

