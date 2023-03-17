def reverse_text(text):
    for character in reversed(text):
        yield character


for char in reverse_text("step"):
    print(char, end='')
