from collections import deque

stack = deque(x for x in input())
for index in range(len(stack) - 1):
    current_letter = stack.pop()
    stack.insert(index, current_letter)
print("".join(stack))
