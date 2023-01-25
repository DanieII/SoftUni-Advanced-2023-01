size = int(input())
matrix = [[x for x in input()] for _ in range(size)]
moves = {
    (-2, -1),
    (-1, -2),
    (-2, 1),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
}

removed = 0
while True:
    max_attacked = 0
    max_coordinates = []
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == "K":
                current_attacked = 0
                for move in moves:
                    new_i, new_j = i + move[0], j + move[1]
                    if new_i in range(size) and new_j in range(size):
                        if matrix[new_i][new_j] == "K":
                            current_attacked += 1
                if current_attacked > max_attacked:
                    max_attacked = current_attacked
                    max_coordinates = [i, j]
    if max_coordinates:
        removed += 1
        matrix[max_coordinates[0]][max_coordinates[1]] = "0"
    else:
        break

print(removed)
