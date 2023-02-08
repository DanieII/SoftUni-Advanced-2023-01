from math import log


def calculate_logarithm(number: int, base):
    if base == "natural":
        return f"{log(number):.2f}"
    else:
        return f"{log(number, int(base)):.2f}"


print(calculate_logarithm(int(input()), input()))
