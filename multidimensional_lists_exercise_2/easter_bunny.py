size = int(input())
matrix = []
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(size):
    matrix.append(input().split())
    if "B" in matrix[row]:
        rabbit_coordinates = [row, matrix[row].index("B")]

max_eggs = 0
best_path = []
for move in moves:
    current_eggs = 0
    current_path = []
    r, c = moves[move]
    new_r, new_c = rabbit_coordinates[0] + r, rabbit_coordinates[1] + c

    while new_r in range(size) and new_c in range(size):
        if matrix[new_r][new_c].isdigit():
            current_eggs += int(matrix[new_r][new_c])
        else:
            break
        current_path.append([new_r, new_c])
        new_r += r
        new_c += c

    if current_eggs >= max_eggs:
        best_path.clear()
        max_eggs = current_eggs
        best_path.append(move)
        best_path.extend(current_path)

print(*best_path, sep="\n")
print(max_eggs)
