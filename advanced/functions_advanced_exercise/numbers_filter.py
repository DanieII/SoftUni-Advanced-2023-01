def even_odd_filter(**kwargs):
    odd_numbers = kwargs.get("odd")
    even_numbers = kwargs.get("even")
    if odd_numbers:
        kwargs["odd"] = list(filter(lambda x: x % 2 != 0, kwargs["odd"]))
    if even_numbers:
        kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))
    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


# Test
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
