words_counter = {}
with open("words.txt", "r") as file:
    words = file.readline().split()
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        for word in words:
            if word not in words_counter:
                words_counter[word] = 0
            words_counter[word] += line.count(word)

with open("output.txt", "w") as file:
    output = []
    for k, v in sorted(words_counter.items(), key=lambda x: -x[1]):
        output.append(f"{k}-{v}")
    file.write("\n".join(output))
