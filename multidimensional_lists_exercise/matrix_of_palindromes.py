rows, columns = [int(x) for x in input().split()]
matrix = [[] for i in range(rows)]
for row in range(rows):
    for column in range(columns):
        starting_and_last_letter = chr(97 + row)
        middle_letter = chr(97 + (row + column))
        current_column = starting_and_last_letter + middle_letter + starting_and_last_letter
        matrix[row].append(current_column)
[print(*x) for x in matrix]
