rows, columns = [int(x) for x in input().split(", ")]
matrix = [[int(j) for j in input().split(", ")] for i in range(rows)]
biggest_sum = None
biggest_square = []
for row in range(rows - 1):
    current_square = []
    square_to_sum = []
    for column in range(columns - 1):
        current_square = [[matrix[row][column], matrix[row + 1][column]],
                          [matrix[row][column + 1], matrix[row + 1][column + 1]]]
        current_sum = sum(int(x) for row in current_square for x in row)

        if biggest_sum:
            if biggest_sum < current_sum:
                biggest_sum = current_sum
                biggest_square = [[j for j in current_square[i]] for i in range(len(current_square))]
        else:
            # Set the first sum and square if they don't exist yet
            biggest_sum = current_sum
            biggest_square = [[j for j in current_square[i]] for i in range(len(current_square))]

        current_square.clear()
        square_to_sum.clear()
[print(*x) for x in zip(biggest_square[0], biggest_square[1])]
print(biggest_sum)
