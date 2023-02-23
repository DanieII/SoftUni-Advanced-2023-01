rows, columns = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0
for row in range(rows):
    matrix.append([])
    integers = [int(x) for x in input().split(", ")]
    for el in integers:
        matrix[row].append(el)
    total_sum += sum(matrix[row])
print(total_sum)
print(matrix)
