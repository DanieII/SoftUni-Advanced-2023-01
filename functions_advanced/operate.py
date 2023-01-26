from functools import reduce


def operate(operator, *args):
    def add():
        return reduce(lambda x, y: x + y, [int(x) for x in args])

    def subtract():
        return reduce(lambda x, y: x - y, [int(x) for x in args])

    def multiply():
        return reduce(lambda x, y: x * y, [int(x) for x in args])

    def divide():
        return reduce(lambda x, y: x / y, [int(x) for x in args])

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("*", 3, 4))
