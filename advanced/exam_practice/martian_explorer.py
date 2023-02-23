moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

SIZE = 6
rover_pos = []
matrix = []
for i in range(SIZE):
    matrix.append(input().split())
    if "E" in matrix[i]:
        rover_pos = [i, matrix[i].index("E")]
deposits = {
    "W": 0,
    "M": 0,
    "C": 0,
}
corresponding = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete",
}

commands = input().split(", ")

for command in commands:
    r, c = moves[command]
    current_r, current_c = rover_pos[0] + r, rover_pos[1] + c

    if not (current_r in range(SIZE) and current_c in range(SIZE)):
        if current_r < 0:
            current_r = SIZE - 1
        elif current_r >= SIZE:
            current_r = 0

        if current_c < 0:
            current_c = SIZE - 1
        elif current_c >= SIZE:
            current_c = 0

    rover_pos = [current_r, current_c]
    stepped = matrix[current_r][current_c]
    if stepped in deposits:
        deposits[stepped] += 1
        print(f"{corresponding[stepped]} deposit found at ({current_r}, {current_c})")
    elif stepped == "R":
        print(f"Rover got broken at ({current_r}, {current_c})")
        break

if all([x for x in deposits.values()]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
