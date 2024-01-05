from collections import deque

day = 1
portions_list = list([int(x) for x in input().split(', ')])
stamina = deque([int(x) for x in input().split(', ')])

conquered_peaks = []
peaks = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])
stamina_needed = deque([80, 90, 100, 60, 70])

while True:
    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if day > 7 or not portions_list or not stamina_needed:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
    else:
        day += 1
        sum_ = portions_list.pop() + stamina.popleft()
        if sum_ >= stamina_needed[0]:
            stamina_needed.popleft()
            conquered_peaks.append(peaks.popleft())
        else:
            continue

if conquered_peaks:
    print(f"Conquered peaks:")
    print('\n'.join(conquered_peaks))
