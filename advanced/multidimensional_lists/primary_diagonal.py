n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
result = 0
for i in range(n):
    result += matrix[i][i]
print(result)
