from collections import deque

string = deque(x for x in input())
for index in range(len(string) - 1):
    current_letter = string.pop()
    string.insert(index, current_letter)
print("".join(string))


# Solution with a stack
# string = list(input())
# reversed_string = []
# while string:
#     reversed_string.append(string.pop())
# print("".join(reversed_string))
