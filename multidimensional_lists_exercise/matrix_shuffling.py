def validation(lst):
    if not lst[0] == "swap":
        return False
    if not len(lst) == 5:
        return False
    else:
        # Turn the items in the list into integers
        for index in range(1, len(lst)):
            number = int(lst[index])
            lst[index] = number
        global split
        split = lst
        for coordinate in range(1, len(lst), 2):
            row = lst[coordinate]
            column = lst[coordinate + 1]
            if row < 0 or column < 0:
                return False
            try:
                matrix[row][column]
            except IndexError:
                return False
    return True


rows, columns = [int(x) for x in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]
while True:
    command = input()
    if command == "END":
        break

    split = command.split()
    if validation(split):
        a = 1
        matrix[split[1]][split[2]], matrix[split[3]][split[4]] = matrix[split[3]][split[4]], matrix[split[1]][split[2]]
        for i in range(len(matrix)):
            print(*matrix[i])
    else:
        print("Invalid input!")
