moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

SIZE = int(input())
snake_pos = []
matrix = []
burrows = []
for i in range(SIZE):
    matrix.append(list(input()))

    if "S" in matrix[i]:
        snake_pos = [i, matrix[i].index("S")]
        matrix[snake_pos[0]][snake_pos[1]] = "."

    if "B" in matrix[i]:
        burrows.append([i, matrix[i].index("B")])

food = 0
win = False
while True:
    command = input()
    r, c = moves[command]

    snake_pos = [snake_pos[0] + r, snake_pos[1] + c]
    if snake_pos[0] not in range(SIZE) or snake_pos[1] not in range(SIZE):
        print("Game over!")
        break

    stepped = matrix[snake_pos[0]][snake_pos[1]]

    if stepped == "*":
        food += 1
        matrix[snake_pos[0]][snake_pos[1]] = "-"

        if food == 10:
            win = True
            break

    elif stepped == "B":
        matrix[snake_pos[0]][snake_pos[1]] = "."
        burrows.remove([snake_pos[0], snake_pos[1]])
        snake_pos = burrows[0]

    matrix[snake_pos[0]][snake_pos[1]] = "."

if win:
    matrix[snake_pos[0]][snake_pos[1]] = "S"
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
[print(*row, sep="") for row in matrix]
