expression = input()
stack = []
for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        last_opening_parenthesis = stack.pop()
        print(expression[last_opening_parenthesis:index + 1])
