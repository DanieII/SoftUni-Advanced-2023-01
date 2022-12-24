n = int(input())
matrix = [[j for j in input()] for i in range(n)]
symbol = input()
found = False
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        current_number = matrix[row][col]
        if not current_number == symbol:
            continue
        print(f"({row}, {col})")
        found = True
        break
    if found:
        break
if not found:
    print(f"{symbol} does not occur in the matrix")
