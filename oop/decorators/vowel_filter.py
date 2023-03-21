def vowel_filter(function):

    def wrapper():

        letters = function()
        vowels = filter(lambda x: x in ["a", "u", "o", "y", "e", "i"], letters)

        return list(vowels)

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
