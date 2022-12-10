water = int(input())
lst = []
while True:
    command = input()
    if command == "Start":
        break
    else:
        lst.append(command)

current_position = 0
while True:
    command = input()
    if command == "End":
        print(f"{water} liters left")
        break
    if command.isdigit():
        liters = int(command)
        name = lst[current_position]
        if water >= liters:
            water -= liters
            print(f"{name} got water")
            lst.remove(name)
        else:
            print(f"{name} must wait")
            lst.remove(name)
    else:
        liters = int(command.split()[1])
        water += liters
