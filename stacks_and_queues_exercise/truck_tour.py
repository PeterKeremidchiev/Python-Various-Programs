from collections import deque

stations_info = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

stations_info_copy = stations_info.copy()
gas = 0
index = 0

while stations_info_copy:
    petrol, distance = stations_info_copy.popleft()

    gas += petrol

    if gas >= distance:
        gas -= distance
    else:
        stations_info.rotate(-1)
        stations_info_copy = stations_info.copy()
        index += 1
        gas = 0
print(index)