size = int(input())
matrix = []
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

alice_position = []
for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_position = [row, matrix[row].index("A")]
        matrix[alice_position[0]][alice_position[1]] = "*"

collected = 0
while True:
    current_movement = input()
    new_r, new_c = alice_position[0] + moves[current_movement][0], alice_position[1] + moves[current_movement][1]
    if new_r in range(size) and new_c in range(size):
        current_position = matrix[new_r][new_c]
        matrix[new_r][new_c] = "*"
        alice_position = [new_r, new_c]
        if current_position == "R":
            break
        if current_position.isdigit():
            collected += int(current_position)
            if collected >= 10:
                break
    else:
        break

print("She did it! She went to the party." if collected >= 10 else "Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
