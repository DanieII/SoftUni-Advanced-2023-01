def multiply(times):

    def decorator(function):

        def wrapper(*args, **kwargs):

            number = args[0]
            return times * function(number)

        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
