def list_manipulator(*args):
    lst = args[0]
    other = False
    if len(args) > 3:
        action, where, *numbers = args[1:]
        other = True
    else:
        action, where = args[1:]

    if action == "add" and where == "beginning":
        numbers.extend(lst)
        lst = numbers

    elif action == "add" and where == "end":
        lst.extend(numbers)

    elif action == "remove" and where == "beginning":
        if other:
            number = numbers[0]
            lst = lst[number:]
        else:
            lst.pop(0)

    elif action == "remove" and where == "end":
        if other:
            number = len(lst) - numbers[0]
            lst = lst[:number]
        else:
            lst.pop()

    return lst


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
