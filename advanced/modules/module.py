def create_triangle(size):
    triangle = ""

    # first part
    for r in range(1, size + 1):
        for c in range(1, r + 1):
            triangle += f"{c} "
        triangle += "\n"
    # second part
    for r in range(size - 1, -1, -1):
        for c in range(1, r + 1):
            triangle += f"{c} "
        triangle += "\n"

    return triangle


def mathematical_operations(*args):
    first, operator, second = args

    operations = {
        "/": lambda x, y: x / y,
        "*": lambda x, y: x * y,
        "-": lambda x, y: x - y,
        "^": lambda x, y: x ** y,
    }

    return f"{operations[operator](float(first), float(second)):.2f}"


def fibonacci_sequence_module(*args):
    # fibonacci logic
    def fibonacci_sequence(n):
        sequence = [0, 1]
        for i in range(n - 2):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence

    def locate_number(n, seq):
        try:
            return f"The number - {n} is at index {seq.index(n)}"
        except ValueError:
            return f"The number {n} is not in the sequence"

    action = args[0]
    if action == "Create":
        return fibonacci_sequence
    elif action == "Locate":
        return locate_number
