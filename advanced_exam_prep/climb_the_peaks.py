from collections import deque

peaks_to_climb = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])
climbed_peaks = []
food_portions = deque([int(x) for x in input().split(", ")])
stamina = deque([int(x) for x in input().split(", ")])
day = 1

while True:
    if len(climbed_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not food_portions or not stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
    portion = food_portions.pop()
    daily_stamina = stamina.popleft()
    current_sum = portion + daily_stamina

    current_index = 0

    if current_sum >= peaks_to_climb[current_index][1]:
        climbed_peaks.append(peaks_to_climb[current_index][0])
        peaks_to_climb.popleft()
        current_index += 1
        day += 1
    else:
        day += 1
        continue

if climbed_peaks:
    print("Conquered peaks:")
    print("\n".join(climbed_peaks))
