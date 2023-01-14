numbers = [int(x) for x in input().split()]
for i in range(len(numbers)):
    print(numbers.pop(), end=" ")

# Old solution
# from collections import deque
#
# numbers = deque(x for x in input().split())
# for index in range(len(numbers)):
#     current_number = numbers.pop()
#     numbers.insert(index, current_number)
# print(" ".join(numbers))
