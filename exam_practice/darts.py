from collections import deque

players = deque([x, 501, 0] for x in input().split(", "))
size = 7
matrix = [input().split() for i in range(size)]


def get_corresponding(r, c):
    def get_up():
        for i in range(r, -1, -1):
            if matrix[i][c].isdigit():
                return int(matrix[i][c])

    def get_down():
        for i in range(r, size):
            if matrix[i][c].isdigit():
                return int(matrix[i][c])

    def get_left():
        for i in range(c, -1, -1):
            if matrix[r][i].isdigit():
                return int(matrix[r][i])

    def get_right():
        for i in range(c, size):
            if matrix[r][i].isdigit():
                return int(matrix[r][i])

    return get_up() + get_right() + get_left() + get_down()


while True:
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    players[0][2] += 1
    if row not in range(size) or col not in range(size):
        players.rotate(-1)
        continue
    hit = matrix[row][col]
    if hit.isdigit():
        players[0][1] -= int(hit)
    elif hit == "D":
        players[0][1] -= get_corresponding(row, col) * 2
    elif hit == "T":
        players[0][1] -= get_corresponding(row, col) * 3
    elif hit == "B":
        break
    if players[0][1] <= 0:
        break
    players.rotate(-1)
print(f"{players[0][0]} won the game with {players[0][2]} throws!")
