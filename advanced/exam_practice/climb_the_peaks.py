from collections import deque

food_portions = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))

conquered = []
peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70,
}

while peaks and food_portions and stamina:
    current_portion = food_portions.pop()
    current_stamina = stamina.popleft()
    result = current_stamina + current_portion
    corresponding_peak = list(peaks.keys())[0]
    corresponding_peak_value = peaks[corresponding_peak]
    if result >= corresponding_peak_value:
        conquered.append(corresponding_peak)
        del peaks[corresponding_peak]
if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered:
    print("Conquered peaks:")
    [print(x) for x in conquered]
