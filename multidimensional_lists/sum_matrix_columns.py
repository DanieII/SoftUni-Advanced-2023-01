rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(j) for j in input().split()] for i in range(rows)]
for col in range(cols):
    result = 0
    for row in range(rows):
        # Going through every row with the current column index
        result += matrix[row][col]
    print(result)
