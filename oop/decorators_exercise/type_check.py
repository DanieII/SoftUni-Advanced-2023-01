def type_check(wanted_type):
    def decorator(func):
        def wrapper(*args):
            if not isinstance(args[0], wanted_type):
                return "Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
