def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


# Test input
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
