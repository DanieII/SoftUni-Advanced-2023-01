from string import punctuation

with open("text.txt", "r") as file:
    lines = file.readlines()
for line in lines[::2]:
    for element in punctuation:
        line = line.replace(element, "@")
    print(*line.split()[::-1])
