import os

while True:
    command, *other = input().split("-")
    if command == "End":
        break

    if command == "Create":
        f = open(other[0], "w")
        f.close()
    elif command == "Add":
        with open(other[0], "a") as file:
            file.write(other[1] + "\n")
    elif command == "Replace":
        try:
            # read the content
            with open(other[0], "r") as file:
                content = file.read()
                content = content.replace(other[1], other[2])
            # replace with the new content
            with open(other[0], "w") as file:
                file.write(content)
        except FileNotFoundError:
            print("An error occurred")
    elif command == "Delete":
        try:
            os.remove(other[0])
        except FileNotFoundError:
            print("An error occurred")
