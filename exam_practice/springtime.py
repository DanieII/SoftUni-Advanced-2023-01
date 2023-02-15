def start_spring(**kwargs):
    result = []
    types = {}

    for name, object_type in kwargs.items():
        if object_type not in types:
            types[object_type] = []
        types[object_type].append(name)

    sorted_types = dict(sorted(types.items(), key=lambda x: (-len(x[1]), x[0])))

    for k, v in sorted_types.items():
        result.append(f"{k}:")
        for object_name in sorted(v):
            result.append(f"-{object_name}")

    return "\n".join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
