with open("numbers.txt", "r") as file:
    numbers = [int(x) for x in file.readlines()]
    print(sum(numbers))
