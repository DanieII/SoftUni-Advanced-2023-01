from module import fibonacci_sequence_module

while True:
    info = input().split()
    command = info[0]
    if command == "Stop":
        break
    number = int(info[-1])
    if command == "Create":
        current_sequence = fibonacci_sequence_module("Create")(number)
        print(*current_sequence)
    elif command == "Locate":
        print(fibonacci_sequence_module("Locate")(number, current_sequence))
