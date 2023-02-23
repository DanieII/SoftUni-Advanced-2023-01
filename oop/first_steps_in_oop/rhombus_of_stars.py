def rhombus_of_stars(n):
    for row in range(1, n + 1):
        white_spaces = n - row
        print(" " * white_spaces, end="")
        for col in range(row):
            print("* ", end="")
        print()

    for row in range(n - 1, -1, -1):
        white_spaces = n - row
        print(" " * white_spaces, end="")
        for col in range(row):
            print("* ", end="")
        print()


rhombus_of_stars(int(input()))
