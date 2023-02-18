def shop_from_grocery_list(budget, lst, *args):
    budget = int(budget)
    purchased = []
    for name, price in args:
        if name not in purchased and name in lst:
            if budget >= price:
                budget -= price
                purchased.append(name)
            else:
                break
    if len(lst) == len(purchased):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        # missing = set(lst).difference(set(purchased))
        missing = []
        for lst_item in lst:
            if lst_item not in purchased:
                missing.append(lst_item)
        return f"You did not buy all the products. Missing products: {', '.join(sorted(missing))}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

