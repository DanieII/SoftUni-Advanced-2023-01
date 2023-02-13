from collections import deque

elves = deque(int(x) for x in input().split())
boxes = [int(x) for x in input().split()]
used = 0
toys_made = 0
box_taken = 0

while elves and boxes:
    elf = elves.popleft()
    while elf < 5 and elves:
        elf = elves.popleft()
    if not elves and elf < 5:
        break
    box_taken += 1
    box = boxes.pop()
    current_toys = 1
    cookies = 1
    two_toys = False

    needed = box

    if box_taken % 3 == 0:
        needed *= 2
        if elf >= needed:
            two_toys = True

    if needed > elf:
        elves.append(elf * 2)
        boxes.append(box)
    else:
        if two_toys:
            current_toys = 2

        if box_taken % 5 == 0:
            current_toys = 0
            cookies = 0

        elf -= needed
        used += needed
        toys_made += current_toys
        elves.append(elf + cookies)

print(f"Toys: {toys_made}")
print(f"Energy: {used}")
if elves:
    print(f"Elves left: {', '.join([str(x) for x in elves])}")
if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")
