def even_numbers(function):

    def wrapper(numbers):

        even = filter(lambda x: x % 2 == 0, numbers)
        return list(even)

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))

