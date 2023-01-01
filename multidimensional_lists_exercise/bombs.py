def bomb(r, c):
    bomb_amount = matrix[r][c]
    matrix[r][c] = 0
    for i in range(r - 1, r + 2):
        if 0 <= i < number_of_rows_and_cols:
            for j in range(c - 1, c + 2):
                if 0 <= j < number_of_rows_and_cols:
                    if [i, j] not in dead_cells:
                        if matrix[i][j] > 0:
                            matrix[i][j] -= bomb_amount
                            if matrix[i][j] <= 0:
                                dead_cells.append([i, j])


number_of_rows_and_cols = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(number_of_rows_and_cols)]
coordinates = [[int(i) for i in x.split(",")] for x in input().split()]
dead_cells = []
for coordinate in coordinates:
    row, column = coordinate
    if matrix[row][column] > 0:
        bomb(row, column)
left = [x for y in matrix for x in y if x > 0]
print(f"Alive cells: {len(left)}\nSum: {sum(left)}")
[print(*x) for x in matrix]
