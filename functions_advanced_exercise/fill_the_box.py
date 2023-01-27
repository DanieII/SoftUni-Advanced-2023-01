def fill_the_box(*args):
    height, length, width, *rest = args
    free_space = height * length * width
    initial_space = free_space
    used = 0
    for i in range(len(rest)):
        if rest[i] == "Finish":
            return f"There is free space in the box. You could put {initial_space - used} more cubes."
        if free_space - rest[i] <= 0:
            difference = rest[i] - free_space
            left_cubes = rest[i]
            if free_space - (rest[i] - difference) <= 0:
                left_cubes = rest[i] - (rest[i] - difference)
            for k in rest[i + 1:]:
                if k == "Finish":
                    break
                left_cubes += k
            return f"No more free space! You have {left_cubes} more cubes."
        else:
            free_space -= rest[i]
            used += rest[i]


# Test
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
