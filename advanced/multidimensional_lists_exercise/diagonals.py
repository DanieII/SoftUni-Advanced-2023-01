rows = int(input())
matrix = [[int(j) for j in input().split(", ")] for i in range(rows)]
# Primary diagonal
primary_diagonal = []
for i in range(len(matrix)):
    current_number = matrix[i][i]
    primary_diagonal.append(current_number)
# Secondary diagonal
secondary_diagonal = []
for k in range(len(matrix)):
    current_number = matrix[k][-(k + 1)]
    secondary_diagonal.append(current_number)

sum_of_primary = sum(primary_diagonal)
print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum_of_primary}")

sum_of_secondary = sum(secondary_diagonal)
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum_of_secondary}")
