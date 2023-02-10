from collections import deque


def create_matrix(row_size=6, column_size=7):
    matrix = []

    def ask_for_size():
        while True:
            row_size = int(input("Enter row size: "))
            column_size = int(input("Enter column size: "))
            if row_size <= 5 or column_size <= 5:
                print("The values must be bigger than five. Try again.")
            else:
                break
        return row_size, column_size

    while True:
        answer = input("Do you want to use the default size of the table? Y/N: ").upper()
        if answer == "Y" or answer == "N":
            if answer == "N":
                row_size, column_size = ask_for_size()
            break

    for i in range(row_size):
        matrix.append([0] * column_size)
    return matrix


def place_number(column, number, matrix):
    for r in range(len(matrix) - 1, -1, -1):
        if not matrix[r][column - 1]:
            matrix[r][column - 1] = number
            break
    return matrix, (r, column), number


def ask_player(matrix):
    player_number = players[0]
    column = int(input(f"Player {player_number}, please choose a column\n"))
    players.rotate(-1)
    return place_number(column, player_number, matrix)


def check_for_win(matrix, position, player):
    position_row, position_col = position

    def check_horizontal():
        columns_size = len(matrix[0])
        for i in range(columns_size):
            if matrix[position_row][i] == player:
                end_of_sequence = i + 4
                if end_of_sequence >= columns_size:
                    end_of_sequence = columns_size
                rest = matrix[position_row][i + 1:end_of_sequence]
                return all([x == player for x in rest]) if len(rest) >= 3 else False

    def check_vertical():
        rows_size = len(matrix)
        for i in range(rows_size):
            if matrix[i][position_col - 1] == player:
                end_of_sequence = i + 4
                if end_of_sequence >= rows_size:
                    end_of_sequence = rows_size
                rest = []
                for j in range(i + 1, end_of_sequence):
                    rest.append(matrix[j][position_col - 1])
                return all([x == player for x in rest]) if len(rest) >= 3 else False

    # TODO: implement diagonals logic

    if any((check_horizontal(), check_vertical())):
        return True
    return False


def start_game(players):
    matrix = create_matrix()
    while True:
        matrix, last_position, number = ask_player(matrix)
        result = check_for_win(matrix, last_position, number)

        [print(row) for row in matrix]

        if result:
            print(f"The winner is player {number}")
            break


players = deque([1, 2])
start_game(players)
