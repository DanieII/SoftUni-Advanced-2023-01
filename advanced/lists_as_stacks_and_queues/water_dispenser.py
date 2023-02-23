from collections import deque

quantity = int(input())
queue = deque()
while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)

while True:
    command = input()
    if command == "End":
        print(f"{quantity} liters left")
        break

    if command.startswith("refill"):
        quantity += int(command.split()[1])
    else:
        current_user = queue.popleft()
        needed = int(command)
        if needed > quantity:
            print(f"{current_user} must wait")
            continue
        print(f"{current_user} got water")
        quantity -= needed

# Old solution
# water = int(input())
# lst = []
# while True:
#     command = input()
#     if command == "Start":
#         break
#     else:
#         lst.append(command)
#
# current_position = 0
# while True:
#     command = input()
#     if command == "End":
#         print(f"{water} liters left")
#         break
#     if command.isdigit():
#         liters = int(command)
#         name = lst[current_position]
#         if water >= liters:
#             water -= liters
#             print(f"{name} got water")
#             lst.remove(name)
#         else:
#             print(f"{name} must wait")
#             lst.remove(name)
#     else:
#         liters = int(command.split()[1])
#         water += liters
