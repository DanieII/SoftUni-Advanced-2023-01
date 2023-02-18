moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

players = 3
steps = 0
player_pos = []
rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    matrix.append(input().split())
    if "B" in matrix[i]:
        player_pos = [i, matrix[i].index("B")]
        matrix[player_pos[0]][player_pos[1]] = "-"

while True:
    command = input()
    if command == "Finish":
        break

    r, c = moves[command]
    new_r, new_c = [player_pos[0] + r, player_pos[1] + c]
    if new_r not in range(rows) or new_c not in range(cols) or matrix[new_r][new_c] == "O":
        continue
    player_pos = [new_r, new_c]
    steps += 1
    if matrix[player_pos[0]][player_pos[1]] == "P":
        players -= 1
        matrix[player_pos[0]][player_pos[1]] = "-"
        if not players:
            break

print("Game over!")
print(f"Touched opponents: {3 - players} Moves made: {steps}")
