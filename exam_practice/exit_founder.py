from collections import deque

SIZE = 6
# The boolean value shows if the player needs to rest
players = deque([x, False] for x in input().split(", "))
tom_pos, jerry_pos = [], []
matrix = [input().split() for _ in range(SIZE)]


def move_player(value, player):
    if value == "E":
        print(f"{current_player} found the Exit and wins the game!")
        return True

    elif value == "T":
        print(f"{current_player} is out of the game! The winner is {players[1][0]}.")
        return True

    elif value == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        players[0][1] = True
    return False


while True:
    player_state = players[0][1]
    r, c = [int(x) for x in input()[1:-1].split(", ")]

    if player_state:
        players[0][1] = False
        players.rotate(-1)
        continue
    current_player = players[0][0]

    if current_player == "Tom":
        tom_pos = [r, c]
        stepped = matrix[r][c]
        if move_player(stepped, current_player):
            break

    elif current_player == "Jerry":
        jerry_pos = [r, c]
        stepped = matrix[r][c]
        if move_player(stepped, current_player):
            break

    players.rotate(-1)
