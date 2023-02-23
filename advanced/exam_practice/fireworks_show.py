from collections import deque


def check_for_fireworks():
    if collected["Palm Fireworks"] >= 3 and collected["Willow Fireworks"] >= 3 and collected["Crossette Fireworks"] >= 3:
        return True
    return False


collected = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}
firework_effects = deque(int(x) for x in input().split(", "))
explosive_power = [int(x) for x in input().split(", ")]

while True:
    if check_for_fireworks() or not explosive_power or not firework_effects:
        break

    current_effect = firework_effects.popleft()
    current_power = explosive_power.pop()
    if current_effect <= 0 or current_power <= 0:
        if current_effect > 0:
            firework_effects.appendleft(current_effect)
        elif current_power > 0:
            explosive_power.append(current_power)
        continue
    result = current_power + current_effect

    if result % 3 == 0 and result % 5 != 0:
        collected["Palm Fireworks"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        collected["Willow Fireworks"] += 1
    elif result % 5 == 0 and result % 3 == 0:
        collected["Crossette Fireworks"] += 1
    else:
        decreased_effect = current_effect - 1
        if decreased_effect > 0:
            firework_effects.append(current_effect - 1)
        explosive_power.append(current_power)
if check_for_fireworks():
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
for k, v in collected.items():
    print(f"{k}: {v}")
