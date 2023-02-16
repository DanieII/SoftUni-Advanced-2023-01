def shopping_cart(*args):
    products = {"Soup": [], "Pizza": [], "Dessert": []}
    limits = {
        "Soup": lambda x: len(x) < 3,
        "Pizza": lambda x: len(x) < 4,
        "Dessert": lambda x: len(x) < 2,
    }

    def check_for_empty():
        empty = True
        for bought in products.values():
            if bought:
                empty = False
        return empty

    for elements in args:
        if elements == "Stop":
            break
        type_of_meal, product = elements

        if product not in products[type_of_meal] and limits[type_of_meal](products[type_of_meal]):
            products[type_of_meal].append(product)

    if not check_for_empty():
        result = []
        sorted_products = dict(sorted(products.items(), key=lambda x: (-len(x[1]), x[0])))

        for k, v in sorted_products.items():
            result.append(f"{k}:")
            if v:
                items = []
                for item in sorted(v):
                    items.append(f" - {item}")

                result.append("\n".join(items))

        return "\n".join(result)

    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'cheese'),
    ('Dessert', 'yoghurt'),
    'Stop',
))

