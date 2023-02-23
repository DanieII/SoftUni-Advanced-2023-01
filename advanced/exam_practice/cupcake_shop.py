from collections import deque


def stock_availability(*args):
    inventory = deque(args[0])
    action = args[1]
    if action == "delivery":
        for index in range(2, len(args)):
            inventory.append(args[index])
    elif action == "sell":
        try:
            another_parameter = args[2]
        except IndexError:
            inventory.popleft()
            return list(inventory)
        if str(another_parameter).isdigit():
            for _ in range(int(another_parameter)):
                inventory.popleft()
        else:
            ordered_flavours = args[2:]
            for flavour in inventory.copy():
                if flavour in ordered_flavours:
                    inventory.remove(flavour)
    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
