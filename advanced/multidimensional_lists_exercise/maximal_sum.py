rows, columns = [int(x) for x in input().split()]
matrix = [[int(j) for j in input().split()] for i in range(rows)]
max_sum = None
max_square = []
for row in range(rows - 2):
    for column in range(columns - 2):
        current_square = [[matrix[row][column], matrix[row][column + 1], matrix[row][column + 2]],
                          [matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2]],
                          [matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]]
        current_sum = 0
        for i in range(len(current_square)):
            for j in range(len(current_square[i])):
                current_sum += current_square[i][j]
        if max_sum:
            if current_sum > max_sum:
                max_sum = current_sum
                max_square = current_square
        else:
            max_sum = current_sum
            max_square = current_square
print(f"Sum = {max_sum}")
[print(" ".join([str(x) for x in k])) for k in max_square]
