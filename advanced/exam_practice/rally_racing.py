size = int(input())
racing_car_number = input()
car_position = [0, 0]
kilometers_passed = 0
tunnels = []
matrix = []
for i in range(size):
    matrix.append(input().split())
    if "T" in matrix[i]:
        tunnels.append([i, matrix[i].index("T")])

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()
while command != "End":
    r, c = moves[command]
    car_position = [car_position[0] + r, car_position[1] + c]
    if matrix[car_position[0]][car_position[1]] == "T":
        matrix[car_position[0]][car_position[1]] = "."
        next_tunnel = [x for x in tunnels if x != car_position]
        matrix[next_tunnel[0][0]][next_tunnel[0][1]] = "."
        car_position = [next_tunnel[0][0], next_tunnel[0][1]]
        kilometers_passed += 30
    elif matrix[car_position[0]][car_position[1]] == "F":
        print(f"Racing car {racing_car_number} finished the stage!")
        kilometers_passed += 10
        matrix[car_position[0]][car_position[1]] = "C"
        break
    else:
        kilometers_passed += 10

    command = input()
else:
    print(f"Racing car {racing_car_number} DNF.")
    matrix[car_position[0]][car_position[1]] = "C"
print(f"Distance covered {kilometers_passed} km.")
[print(*row, sep="") for row in matrix]

# Another solution that changes the car position after every move but doesn't get 100/100 in judge
# size = int(input())
# racing_car_number = input()
# car_position = [0, 0]
# kilometers_passed = 0
# tunnels = []
# matrix = []
# for i in range(size):
#     matrix.append(input().split())
#     if "T" in matrix[i]:
#         tunnels.append([i, matrix[i].index("T")])
#
# moves = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
#
# def change_position(old, new):
#     next = matrix[new[0]][new[1]]
#     matrix[old[0]][old[1]] = "."
#     matrix[new[0]][new[1]] = "C"
#     return next
#
#
# command = input()
# while command != "End":
#     r, c = moves[command]
#     old_position = [car_position[0], car_position[1]]
#     car_position = [car_position[0] + r, car_position[1] + c]
#     next = change_position(old_position, car_position)
#     if next == "T":
#         next_tunnel = [x for x in tunnels if x != car_position]
#         old_position = car_position
#         car_position = [next_tunnel[0][0], next_tunnel[0][1]]
#         change_position(old_position, car_position)
#         kilometers_passed += 30
#     elif next == "F":
#         print(f"Racing car {racing_car_number} finished the stage!")
#         kilometers_passed += 10
#         break
#     else:
#         kilometers_passed += 10
#
#     command = input()
# else:
#     print(f"Racing car {racing_car_number} DNF.")
# print(f"Distance covered {kilometers_passed} km.")
# [print(*row, sep="") for row in matrix]
