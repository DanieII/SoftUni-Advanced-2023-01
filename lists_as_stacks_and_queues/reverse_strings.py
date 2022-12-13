from collections import deque

strings = deque(x for x in input())
for index in range(len(strings) - 1):
    current_letter = strings.pop()
    strings.insert(index, current_letter)
print("".join(strings))
