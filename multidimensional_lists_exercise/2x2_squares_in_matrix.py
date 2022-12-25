rows, columns = [int(x) for x in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]
number_of_identical = 0
for row in range(rows - 1):
    for column in range(columns - 1):
        current_square = [matrix[row][column], matrix[row][column + 1], matrix[row + 1][column],
                          matrix[row + 1][column + 1]]
        # Check for identity
        same = True
        previous_symbol = current_square[0]
        for index in range(1, len(current_square)):
            current_symbol = current_square[index]
            if current_symbol != previous_symbol:
                same = False
            previous_symbol = current_symbol
        if same:
            number_of_identical += 1
print(number_of_identical)
