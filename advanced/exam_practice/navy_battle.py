size = int(input())
matrix = []
submarine_position = []
for i in range(size):
    matrix.append([x for x in input()])
    if "S" in matrix[i]:
        submarine_position = [i, matrix[i].index("S")]
        matrix[submarine_position[0]][submarine_position[1]] = "-"

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

battle_cruisers = 3
mines_hit = 0
while True:
    current_direction = input()
    new_r, new_c = moves[current_direction]
    next_r, next_c = submarine_position[0] + new_r, submarine_position[1] + new_c
    submarine_position = [next_r, next_c]
    position = matrix[next_r][next_c]
    if position == "-":
        continue
    elif position == "*":
        mines_hit += 1
        if mines_hit <= 2:
            matrix[next_r][next_c] = "-"
        else:
            matrix[next_r][next_c] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{next_r}, {next_c}]!")
            break
    elif position == "C":
        battle_cruisers -= 1
        if battle_cruisers:
            matrix[next_r][next_c] = "-"
        else:
            matrix[next_r][next_c] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
[print("".join(x)) for x in matrix]
