matrix = []
player = []
all_targets = 0
targets_hit = 0
targets_positions = []

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(5):
    matrix.append(input().split())
    if "A" in matrix[i]:
        player = [i, matrix[i].index("A")]
    all_targets += matrix[i].count("x")

number_of_commands = int(input())
for _ in range(number_of_commands):
    current_command = input().split()
    action, *others = current_command
    direction = others[0]
    r, c = moves[direction]
    if action == "move":
        steps = int(others[1])
        new_r, new_c = player[0] + r, player[1] + c
        for k in range(steps):
            if new_r in range(5) and new_c in range(5):
                if matrix[new_r][new_c] == ".":
                    matrix[player[0]][player[1]] = '.'
                    player = [new_r, new_c]
                    matrix[new_r][new_c] = "A"
                new_r += r
                new_c += c
    else:
        shot_r, shot_c = player[0] + r, player[1] + c
        while shot_r in range(5) and shot_c in range(5):
            if matrix[shot_r][shot_c] == "x":
                matrix[shot_r][shot_c] = "."
                targets_hit += 1
                targets_positions.append([shot_r, shot_c])
                break
            shot_r += r
            shot_c += c
if all_targets == targets_hit:
    print(f"Training completed! All {all_targets} targets hit.")
else:
    print(f"Training not completed! {all_targets - targets_hit} targets left.")
[print(position) for position in targets_positions]
[print(*row) for row in matrix]
