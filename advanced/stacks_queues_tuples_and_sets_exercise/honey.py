from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
collected = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar > current_bee:
        symbol = symbols.popleft()
        collected += abs(eval(f"{current_bee}{symbol}{current_nectar}"))
    elif current_nectar < current_bee:
        bees.appendleft(current_bee)
print(f"Total honey made: {collected}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
