from collections import deque

eggs = deque(int(x) for x in input().split(", "))
paper = [int(x) for x in input().split(", ")]

boxes = 0
while eggs and paper:
    current_egg = eggs.popleft()
    while current_egg <= 0 and eggs:
        current_egg = eggs.popleft()
    if current_egg <= 0 and not eggs:
        break

    if current_egg == 13:
        paper[0], paper[-1] = paper[-1], paper[0]
        continue

    current_paper = paper.pop()
    result = current_egg + current_paper

    if result <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper])}")
