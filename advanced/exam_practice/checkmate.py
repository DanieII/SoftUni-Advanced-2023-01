SIZE = 8
queens = []
matrix = []
for i in range(SIZE):
    matrix.append(input().split())
    for j in range(SIZE):
        if matrix[i][j] == "Q":
            queens.append([i, j])

for queen in queens.copy():
    r, c = queen


    def check_for_capture():
        # diagonals

        def down_left():
            king = False
            for j in range(1, (SIZE - (r + 1)) + 1):
                if c - j >= 0:
                    try:
                        current = matrix[r + j][c - j]
                        if current == "K":
                            king = True
                            break
                        elif current == "Q":
                            break
                    except IndexError:
                        break
                else:
                    break

            return king

        def down_right():
            king = False
            for j in range(1, (SIZE - (r + 1)) + 1):
                try:
                    current = matrix[r + j][c + j]
                    if current == "K":
                        king = True
                        break
                    elif current == "Q":
                        break
                except IndexError:
                    break

            return king

        def up_right():
            king = False
            for j in range(1, (SIZE - (SIZE - r)) + 1):
                try:
                    current = matrix[r - j][c + j]
                    if current == "K":
                        king = True
                        break
                    elif current == "Q":
                        break
                except IndexError:
                    break

            return king

        def up_left():
            king = False
            for j in range(1, (SIZE - (SIZE - r)) + 1):
                if c - j >= 0:
                    try:
                        current = matrix[r - j][c - j]
                        if current == "K":
                            king = True
                            break
                        elif current == "Q":
                            break
                    except IndexError:
                        break
                else:
                    break

            return king

        # horizontal
        def horizontal():
            def left():
                king = False
                for j in range(1, (SIZE - (SIZE - c)) + 1):
                    current = matrix[r][c - j]
                    if current == "K":
                        king = True
                        break
                    elif current == "Q":
                        break
                return king

            def right():
                king = False
                for j in range(1, SIZE - (c + 1) + 1):
                    current = matrix[r][c + j]
                    if current == "K":
                        king = True
                        break
                    elif current == "Q":
                        break
                return king

            return any((left(), right()))

        def vertical():
            def up():
                king = False
                for j in range(1, SIZE - (SIZE - r) + 1):
                    current = matrix[r - j][c]
                    if current == "K":
                        king = True
                        break
                    elif current == "Q":
                        break
                return king

            def down():
                king = False
                for j in range(1, SIZE - (r + 1) + 1):
                    current = matrix[r + j][c]
                    if current == "K":
                        king = True
                        break
                    elif current == "Q":
                        break
                return king

            return any((up(), down()))

        return any((down_left(), down_right(), up_right(), up_left(), horizontal(), vertical()))


    if not check_for_capture():
        queens.remove(queen)

if queens:
    for queen in queens:
        print(f"[{queen[0]}, {queen[1]}]")
else:
    print("The king is safe!")
