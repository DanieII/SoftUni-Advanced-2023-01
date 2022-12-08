expression = [x for x in input()]
stack = []
for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        last_opening_parenthesis = stack.pop()
        current_closing_parenthesis = index
        current_set = expression[last_opening_parenthesis:current_closing_parenthesis + 1]
        print("".join(current_set))
