from functools import reduce


def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    result = []
    types = []
    for product, info in kwargs.items():
        price = reduce(lambda x, y: x * y, info)
        if budget - price >= 0:
            if product not in types:
                types.append(product)
            budget -= price
            result.append(f"You bought {product} for {price:.2f} leva.")
            # Check if the program should end
            if len(types) == 5:
                return "\n".join(result)
    return "\n".join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


