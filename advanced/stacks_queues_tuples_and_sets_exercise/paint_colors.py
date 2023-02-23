from collections import deque

substrings = deque(input().split())
colors = {"red", "yellow", "blue", "orange", "purple", "green"}
combinations = {
    "orange": lambda x: {"red", "yellow"}.issubset(x),
    "purple": lambda x: {"red", "blue"}.issubset(x),
    "green": lambda x: {"yellow", "blue"}.issubset(x)
}
found = []

while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ""

    if left + right in colors:
        found.append(left + right)
    elif right + left in colors:
        found.append(right + left)
    else:
        [substrings.insert(len(substrings) // 2, x) for x in (left[:-1], right[:-1]) if x]
for color in found:
    if combinations.get(color):
        if not combinations[color](set(found)):
            found.remove(color)
print(found)
