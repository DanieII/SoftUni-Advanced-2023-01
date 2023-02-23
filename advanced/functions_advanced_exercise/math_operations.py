def math_operations(*args, **kwargs):
    for index in range(len(args)):
        number = args[index]
        current_key = list(kwargs.keys())[index % len(kwargs)]
        if current_key == "a":
            kwargs[current_key] += number
        elif current_key == "s":
            kwargs[current_key] -= number
        elif current_key == "d":
            if number != 0:
                kwargs[current_key] /= number
        elif current_key == "m":
            kwargs[current_key] *= number
    return "\n".join(
        [f"{key}: {value:.1f}" for key, value in dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))).items()])


# Test
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
