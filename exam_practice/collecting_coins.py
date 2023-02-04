size = int(input())
coins = 0
matrix = []
for i in range(size):
    matrix.append(input().split())
    if "P" in matrix[i]:
        player_position = [i, matrix[i].index("P")]

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

path = [player_position]
won = True
while True:
    new_r, new_c = moves[input()]
    current_r, current_c = player_position[0] + new_r, player_position[1] + new_c
    if not (current_r in range(size) and current_c in range(size)):
        if current_r < 0:
            current_r = size - 1
        elif current_r >= size:
            current_r = 0

        if current_c < 0:
            current_c = size - 1
        elif current_c >= size:
            current_c = 0
    player_position = [current_r, current_c]
    path.append(player_position)
    if matrix[current_r][current_c].isdigit():
        coins += int(matrix[current_r][current_c])
        # Change the value of the position so the player doesn't collect it again
        matrix[current_r][current_c] = "-"
        if coins >= 100:
            break
    elif matrix[current_r][current_c] == "X":
        coins //= 2
        won = False
        break
if won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
[print(x) for x in path]
