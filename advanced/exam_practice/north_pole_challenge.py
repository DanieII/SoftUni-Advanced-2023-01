rows, columns = [int(x) for x in input().split(", ")]
santa_position = []

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

short_names = {
    "D": "Christmas decorations",
    "G": "Gifts",
    "C": "Cookies",
}

items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0,
}

# Create matrix
matrix = []
to_be_collected = 0
for i in range(rows):
    matrix.append(input().split())
    if "Y" in matrix[i]:
        santa_position = [i, matrix[i].index("Y")]
        matrix[santa_position[0]][santa_position[1]] = "x"
    for item in short_names.keys():
        if item in matrix[i]:
            to_be_collected += matrix[i].count(item)

# a logic that leads you directly to the desired position but this way following the path is too hard
# moves = {
#     "up": lambda x: (-x, 0),
#     "down": lambda x: (x, 0),
#     "left": lambda x: (0, -x),
#     "right": lambda x: (0, x),
# }

# if not (new_r in range(rows) and new_c in range(columns)):
#     rows_difference = abs(rows - new_r)
#     if new_r < 0:
#         new_r = santa_position[0] - rows_difference
#     elif new_r >= rows:
#         new_r = santa_position[0] + rows_difference
#
#     columns_difference = abs(columns - new_c)
#     if new_c < 0:
#         new_c = santa_position[1] - columns_difference
#     elif new_c >= columns:
#         new_c = santa_position[1] + columns_difference

merry_christmas = False
while True:
    command = input()

    if command == "End":
        break

    direction, steps = command.split("-")
    steps = int(steps)

    r, c = moves[direction]
    for _ in range(steps):
        matrix[santa_position[0]][santa_position[1]] = "x"
        new_r, new_c = santa_position[0] + r, santa_position[1] + c
        # check for out of range
        if not (new_r in range(rows) and new_c in range(columns)):
            if new_r < 0:
                new_r = rows - 1
            elif new_r >= rows:
                new_r = 0

            if new_c < 0:
                new_c = columns - 1
            elif new_c >= columns:
                new_c = 0

        santa_position = [new_r, new_c]
        position = matrix[new_r][new_c]
        if position in short_names.keys():
            items[short_names[position]] += 1
            matrix[new_r][new_c] = "x"
            to_be_collected -= 1
            if not to_be_collected:
                merry_christmas = True
                break
    matrix[santa_position[0]][santa_position[1]] = "Y"
    if merry_christmas:
        break

if merry_christmas:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {items['Christmas decorations']} Christmas decorations")
print(f"- {items['Gifts']} Gifts")
print(f"- {items['Cookies']} Cookies")

[print(*row) for row in matrix]
