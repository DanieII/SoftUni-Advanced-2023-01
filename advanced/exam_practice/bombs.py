from collections import deque

bombs = {
    "Datura Bombs": lambda x: x == 40,
    "Cherry Bombs": lambda x: x == 60,
    "Smoke Decoy Bombs": lambda x: x == 120,
}

collected = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0,
}

effects = deque(int(x) for x in input().split(", "))
casing = [int(x) for x in input().split(", ")]

while effects and casing:
    current_effect = effects.popleft()
    current_casing = casing.pop()
    result = current_effect + current_casing

    for bomb, needed in bombs.items():
        if needed(result):
            collected[bomb] += 1
            break
    else:
        effects.appendleft(current_effect)
        casing.append(current_casing - 5)

    result = all(x >= 3 for x in collected.values())

    if result:
        print("Bene! You have successfully filled the bomb pouch!")
        break

else:
    print("You don't have enough materials to fill the bomb pouch.")

if not effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")

if not casing:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in casing])}")

for k, v in sorted(collected.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")
