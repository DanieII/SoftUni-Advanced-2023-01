from collections import deque

rows, columns = [int(x) for x in input().split()]
matrix = [["" for _ in range(columns)] for _ in range(rows)]
string = deque(x for x in input())
order = True

for i in range(rows):
    for j in range(columns):
        current_letter = string.popleft()
        string.append(current_letter)
        if order:
            matrix[i][j] = current_letter
        else:
            matrix[i][-(j + 1)] = current_letter
    if i % 2 == 0:
        order = False
    else:
        order = True
[print("".join(x)) for x in matrix]
