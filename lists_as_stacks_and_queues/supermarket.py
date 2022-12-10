lst = []
while True:
    command = input()
    if command == "End":
        print(f"{len(lst)} people remaining.")
        break
    elif command == "Paid":
        [print(x) for x in lst]
        lst.clear()
        continue
    else:
        name = command
        lst.append(name)
