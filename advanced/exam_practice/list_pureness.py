def best_list_pureness(*args):
    lst, rotations = args

    def find_pureness(items):
        pureness = 0
        for i in range(len(items)):
            item = items[i]
            pureness += item * i
        return pureness

    best_pureness = None
    for rotation in range(int(rotations) + 1):
        result = find_pureness(lst)

        if not best_pureness:
            best_pureness = [result, rotation]
        elif best_pureness[0] < result:
            best_pureness = [result, rotation]

        lst.insert(0, lst.pop())

    return f"Best pureness {best_pureness[0]} after {best_pureness[1]} rotations"

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

