moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = [input().split() for _ in range(6)]
position = [int(x) for x in input()[1:-1].split(", ")]

while True:
    command = input()
    if command == "Stop":
        break

    action, *info = command.split(", ")
    if action == "Create":
        direction, value = info
        r, c = moves[direction]
        position = [position[0] + r, position[1] + c]
        if matrix[position[0]][position[1]] == ".":
            matrix[position[0]][position[1]] = value
    elif action == "Update":
        direction, value = info
        r, c = moves[direction]
        position = [position[0] + r, position[1] + c]
        if matrix[position[0]][position[1]] != ".":
            matrix[position[0]][position[1]] = value
    elif action == "Delete":
        direction = info[0]
        r, c = moves[direction]
        position = [position[0] + r, position[1] + c]
        if matrix[position[0]][position[1]] != ".":
            matrix[position[0]][position[1]] = "."
    elif action == "Read":
        direction = info[0]
        r, c = moves[direction]
        position = [position[0] + r, position[1] + c]
        if matrix[position[0]][position[1]] != ".":
            print(matrix[position[0]][position[1]])

[print(*row) for row in matrix]
