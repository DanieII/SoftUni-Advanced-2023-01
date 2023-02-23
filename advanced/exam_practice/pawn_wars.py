from collections import deque

SIZE = 8
players = deque(["w", "b"])
white_pos, black_pos = [], []

corresponding = {
    "w": "White",
    "b": "Black"
}

matrix = []
for i in range(SIZE):
    matrix.append(input().split())
    if "w" in matrix[i]:
        white_pos = [i, matrix[i].index("w")]
    elif "b" in matrix[i]:
        black_pos = [i, matrix[i].index("b")]

coordinates = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}


def check_diagonal(capture_coordinates):
    if abs(white_pos[0] - black_pos[0]) == 1 and abs(white_pos[1] - black_pos[1]) == 1:
        location = f"{coordinates[capture_coordinates[1]]}{(SIZE - 1) - (capture_coordinates[0] - 1)}"
        return location


def check_queen(white=True):
    location = ""
    if white:
        r, c = white_pos
        if r == 0:
            location = f"{coordinates[c]}{(SIZE - 1) - (r - 1)}"
            return location
    else:
        r, c = black_pos
        if r == SIZE - 1:
            location = f"{coordinates[c]}{(SIZE - 1) - (r - 1)}"
            return location


while True:
    current_player = corresponding[players[0]]
    if current_player == "White":

        capture_result = check_diagonal(black_pos)
        if capture_result:
            print(f"Game over! {current_player} win, capture on {capture_result}.")
            break

        white_pos[0] -= 1

        queen_result = check_queen()
        if queen_result:
            print(f"Game over! {current_player} pawn is promoted to a queen at {queen_result}.")
            break

    elif current_player == "Black":

        capture_result = check_diagonal(white_pos)
        if capture_result:
            print(f"Game over! {current_player} win, capture on {capture_result}.")
            break

        black_pos[0] += 1

        queen_result = check_queen(False)
        if queen_result:
            print(f"Game over! {current_player} pawn is promoted to a queen at {queen_result}.")
            break

    players.rotate(-1)
