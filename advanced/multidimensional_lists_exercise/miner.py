size = int(input())
directions = input().split()
steps = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}
coal = 0
matrix = [[x for x in input().split()] for _ in range(size)]
for i in range(size):
    for j in range(size):
        if matrix[i][j] == "s":
            miner_position = (i, j)
        elif matrix[i][j] == "e":
            end = [i, j]
        elif matrix[i][j] == "c":
            coal += 1

for direction in directions:
    old_i, old_j = miner_position
    new_difference_i, new_difference_j = steps[direction]
    new_i, new_j = old_i + new_difference_i, old_j + new_difference_j

    if new_i in range(size) and new_j in range(size):
        new_position = matrix[new_i][new_j]
        if new_position == "e":
            print(f"Game over! ({new_i}, {new_j})")
            break
        elif new_position == "c":
            matrix[new_i][new_j] = "*"
            coal -= 1
            if coal == 0:
                print(f"You collected all coal! ({new_i}, {new_j})")
                break
        miner_position = [new_i, new_j]
    else:
        continue
else:
    print(f"{coal} pieces of coal left. ({new_i}, {new_j})")
