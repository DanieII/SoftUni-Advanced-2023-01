from collections import deque

players = deque(input().split())
number = int(input())
toss = 0

while len(players) > 1:
    toss += 1
    current_player = players.popleft()
    if toss == number:
        print(f"Removed {current_player}")
        toss = 0
    else:
        players.append(current_player)
print(f"Last is {players.popleft()}")

# Old solution without a queue
# lst = input().split()
# number_of_toss = int(input())
# last_index = 0
# difference = number_of_toss
# while len(lst) > 1:
#     while difference > len(lst):
#         difference -= len(lst[last_index:])
#         last_index = 0
#     current_name = lst[last_index + difference - 1]
#     last_index = lst.index(current_name)
#     lst.remove(current_name)
#     print(f"Removed {current_name}")
#     difference = number_of_toss
# print(f"Last is {lst[0]}")
