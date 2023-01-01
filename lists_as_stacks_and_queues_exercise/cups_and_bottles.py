from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted = 0

while cups and bottles:
    current_cup = cups[0]
    while current_cup > 0:
        current_bottle = bottles.pop()
        if current_bottle >= current_cup:
            wasted += current_bottle - current_cup
        current_cup -= current_bottle
    cups.popleft()
if not cups:
    print(f'Bottles: {" ".join([str(x) for x in bottles])}')
else:
    print(f'Cups: {" ".join([str(x) for x in cups])}')
print(f'Wasted litters of water: {wasted}')
