presents = int(input())
size = int(input())
matrix = []
santa_position = []
nice_kids = 0
nice_kids_with_presents = 0

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if "S" in matrix[row]:
        santa_position = [row, matrix[row].index("S")]
    nice_kids += matrix[row].count("V")

while presents and nice_kids > nice_kids_with_presents:
    command = input()
    if command.startswith("Christmas"):
        break

    r, c = moves[command]
    new_r, new_c = santa_position[0] + r, santa_position[1] + c
    matrix[santa_position[0]][santa_position[1]] = "-"
    santa_position = [new_r, new_c]

    if matrix[new_r][new_c] == "V":
        nice_kids_with_presents += 1
        presents -= 1
    elif matrix[new_r][new_c] == "C":
        for move in moves:
            i, j = moves[move]
            cell = matrix[santa_position[0] + i][santa_position[1] + j]
            if cell in "XV":
                if cell == "V":
                    nice_kids_with_presents += 1
                presents -= 1
                matrix[santa_position[0] + i][santa_position[1] + j] = "-"
            if not presents:
                break
    matrix[new_r][new_c] = "S"
if not presents and nice_kids - nice_kids_with_presents:
    print("Santa ran out of presents!")
[print(*x) for x in matrix]
if nice_kids == nice_kids_with_presents:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_with_presents} nice kid/s.")
