def even_parameters(func):

    def wrapper(*args):
        even = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, args))

        if len(even) != len(args):
            return "Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
