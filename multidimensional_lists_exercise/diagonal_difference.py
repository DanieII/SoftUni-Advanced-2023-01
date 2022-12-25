rows = int(input())
matrix = [[int(j) for j in input().split()] for i in range(rows)]
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

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)
absolute_difference = abs(primary_sum - secondary_sum)
print(absolute_difference)
