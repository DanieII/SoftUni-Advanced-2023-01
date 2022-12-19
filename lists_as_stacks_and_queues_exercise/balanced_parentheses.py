parentheses = [x for x in input()]
parentheses.reverse()
opening_symbols = ["(", "{", "["]
closing_symbols = [")", "}", "]"]
used_opening = []
used_closing = []
current_is_completed = False
valid_string = False
for index in range(len(parentheses) - 1, -1, -1):
    if parentheses:
        symbol = parentheses[index]
        if symbol in opening_symbols:
            used_opening.append(symbol)
            valid_string = False
        else:
            used_closing.append(symbol)

            if len(used_closing) == len(used_opening):
                closing_matched = []
                for i in used_closing:
                    current_index = closing_symbols.index(i)
                    matched_opening = opening_symbols[current_index]
                    closing_matched.append(matched_opening)
                closing_matched.reverse()
                current_is_completed = True
            valid_string = False
        if current_is_completed:
            if closing_matched == used_opening:
                valid_string = True
            else:
                valid_string = False
            used_opening.clear()
            used_closing.clear()
            closing_matched.clear()
            current_is_completed = False
        parentheses.pop(index)

if valid_string:
    print("YES")
else:
    print("NO")
