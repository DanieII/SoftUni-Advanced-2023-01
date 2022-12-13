stack = []
number_of_queries = int(input())

for _ in range(number_of_queries):
    command = input().split()
    action = command[0]
    if action == "1":
        number = int(command[1])
        stack.append(number)
    elif action == "2":
        if stack:
            stack.pop()
    elif action == "3":
        if stack:
            max_number = max(stack)
            print(max_number)
    elif action == "4":
        if stack:
            minimum_number = min(stack)
            print(minimum_number)
stack.reverse()
print(", ".join([str(x) for x in stack]))
