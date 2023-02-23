def grocery_store(**kwargs):
    new = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    return "\n".join([f"{k}: {v}" for k, v in new.items()])


# Test
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
