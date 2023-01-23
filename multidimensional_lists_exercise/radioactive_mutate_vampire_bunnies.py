rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input()] for _ in range(rows)]
directions = list(input())
moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

changed = []


def spread_bunnies():
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == "B" and (i, j) not in changed:
                for k, new in moves.items():
                    if i + new[0] in range(rows) and j + new[1] in range(columns):
                        if matrix[i + new[0]][j + new[1]] == "B":
                            continue
                        if matrix[i + new[0]][j + new[1]] != "P":
                            matrix[i + new[0]][j + new[1]] = "B"
                        else:
                            # Hit the player
                            matrix[i + new[0]][j + new[1]] = "B"
                            global dead, stop, dead_coordinates
                            dead = True
                            stop = True
                            dead_coordinates = i + new[0], j + new[1]
                        changed.append((i + new[0], j + new[1]))
    changed.clear()


def find_player():
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == "P":
                return i, j


dead = False
for direction in directions:
    current_i, current_j = find_player()
    row, column = moves[direction]
    new_i, new_j = current_i + row, current_j + column
    stop = False
    if new_i in range(rows) and new_j in range(columns):
        if matrix[new_i][new_j] != "B":
            matrix[new_i][new_j] = "P"
            matrix[current_i][current_j] = "."
        else:
            # Hit a bunny
            dead = True
            dead_coordinates = new_i, new_j
            matrix[current_i][current_j] = "."
            stop = True
    else:
        # Escaped
        won_coordinates = current_i, current_j
        matrix[current_i][current_j] = "."
        stop = True
    spread_bunnies()
    if stop:
        break
[print(*[x for x in i], sep="")for i in matrix]
if not dead:
    print(f"won: {won_coordinates[0]} {won_coordinates[1]}")
else:
    print(f"dead: {dead_coordinates[0]} {dead_coordinates[1]}")
