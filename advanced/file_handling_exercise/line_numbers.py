from string import punctuation

with open("text.txt", "r") as file:
    lines = file.readlines()
with open("output.txt", "w") as file:
    for index in range(len(lines)):
        line = lines[index]
        letters = 0
        punctuation_marks = 0
        for element in line:
            if element.isalpha():
                letters += 1
            elif element in punctuation:
                punctuation_marks += 1
        file.write(f"Line {index + 1}: {line[:-1]} ({letters})({punctuation_marks})\n")
