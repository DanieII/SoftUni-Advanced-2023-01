def rectangle(length, width):
    if not type(length) == int or not type(width) == int:
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f"""Rectangle area: {area()}
Rectangle perimeter: {perimeter()}"""


# Test input
print(rectangle(2, 10))
