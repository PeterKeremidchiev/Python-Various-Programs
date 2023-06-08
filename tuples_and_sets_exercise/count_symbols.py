word = sorted(tuple(input()))

count_times = {}

for ch in word:
    if ch not in dict:
        count_times[ch] = 0
    count_times[ch] += 1

for ch, value in count_times.items():
    print(f"{ch}: {value} time/s")
