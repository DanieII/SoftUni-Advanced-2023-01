import pyfiglet


def ascii_art(text):
    return pyfiglet.figlet_format(text)


print(ascii_art(input()))
