from collections import deque

queue = deque()
while True:
    command = input()
    if command == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)

# Old solution
# lst = []
# while True:
#     command = input()
#     if command == "End":
#         print(f"{len(lst)} people remaining.")
#         break
#     elif command == "Paid":
#         [print(x) for x in lst]
#         lst.clear()
#         continue
#     else:
#         name = command
#         lst.append(name)
