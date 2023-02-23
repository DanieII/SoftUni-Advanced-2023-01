def recursive_power(n, power):
    if power == 0:
        return 1

    if power == 1:
        return n

    return n * recursive_power(n, power - 1)


# Test input
print(recursive_power(2, 10))
