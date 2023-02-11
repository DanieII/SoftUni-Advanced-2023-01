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

    matrix = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    # for i in range(row_size):
    #     matrix.append([0] * column_size)
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

    def check_diagonals():

        # def get_starting_row():
        #     if matrix[position_row]
        def check_up_left():
            # не взима правилния стартов ред винаги
            starting_row = max((position_row - 3, 0))
            range_of_numbers = (position_row - starting_row) + 1
            values = []
            for i in range(range_of_numbers):
                values.append(matrix[starting_row + i][len(matrix[0]) - (position_col - 2) - (-i + 3)])
            values_without_zeros = [x for x in values if x]
            return len(set(values_without_zeros)) == 1 and len(values_without_zeros) == 4

        def check_up_right():
            starting_row = max((position_row - 2, 0))
            range_of_numbers = position_row - starting_row
            values = [matrix[starting_row + i][-(i + 1)] for i in range(range_of_numbers + 1)]
            values_without_zeros = [x for x in values if x]
            return len(set(values_without_zeros)) == 1 and len(values_without_zeros) == 4

        def check_down_left():
            if position_col - 2 in range(len(matrix[0])):
                values = [matrix[position_row + i][-(len(matrix[0]) - (position_col - i) + 2)] for i in
                          range(len(matrix) - position_row + 1)]
                values_without_zeros = [x for x in values if x]
                return len(set(values_without_zeros)) == 1 and len(values_without_zeros) == 3
            return False

        def check_down_right():
            starting_row = position_row + 1
            if position_col - 2 in range(len(matrix[0])):
                values = [matrix[starting_row + i][-(len(matrix[0]) - (position_col + i))] for i in
                          range(len(matrix) - starting_row - 1)]
                values_without_zeros = [x for x in values if x]
                return len(set(values_without_zeros)) == 1 and len(values_without_zeros) == 3
            return False

        return any((check_up_left(), check_up_right()))

    if any((check_horizontal(), check_vertical(), check_diagonals())):
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
