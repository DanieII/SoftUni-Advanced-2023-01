first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

actions = {
    "Add": lambda x: [first.add(int(i)) for i in x] if x.pop(0) == "First" else [second.add(int(i)) for i in x],
    "Remove": lambda x: [first.discard(int(i)) for i in x] if x.pop(0) == "First" else [second.discard(int(i)) for i in x],
    "Check": lambda x, y: x.issubset(y) or y.issubset(x)
}

for _ in range(int(input())):
    action, *info = input().split()

    if len(info) > 1:
        actions[action](info)
    else:
        print(actions[action](first, second))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
