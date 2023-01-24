size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
while True:
    command = input().split()
    if command[0] == "END":
        break

    action, *values = command
    row = int(values[0])
    col = int(values[1])
    value = int(values[2])
    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")
        continue
    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value
[print(*row) for row in matrix]
