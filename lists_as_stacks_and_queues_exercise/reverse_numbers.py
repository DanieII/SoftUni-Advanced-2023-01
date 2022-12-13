from collections import deque

numbers = deque(x for x in input().split())
for index in range(len(numbers)):
    current_number = numbers.pop()
    numbers.insert(index, current_number)
print(" ".join(numbers))
