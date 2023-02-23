from functools import reduce

string = input().split()

operators = {
    "*": lambda x, y: int(x) * int(y),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y),
    "/": lambda x, y: int(x) / int(y),
}

current_numbers = []
index = 0
while len(string) > 1:
    element = string[index]
    if element not in operators.keys():
        current_numbers.append(int(element))
        index += 1
        continue
    new_value = reduce(operators[element], string[:index])
    [string.pop(0) for _ in range(index + 1)]
    string.insert(0, new_value)
    current_numbers.clear()
    index = 0
print(int(*string))
