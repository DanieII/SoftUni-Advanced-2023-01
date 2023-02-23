from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk = deque(int(x) for x in input().split(", "))
milkshakes = 0

while milkshakes < 5 and chocolates and milk:
    current_chocolate = chocolates.pop()
    current_milk = milk.popleft()

    if current_milk > 0:
        if current_chocolate > 0:
            if current_milk != current_chocolate:
                milk.append(current_milk)
                chocolates.append(current_chocolate - 5)
            else:
                milkshakes += 1
        else:
            if current_milk > 0:
                milk.appendleft(current_milk)
    else:
        if current_chocolate > 0:
            chocolates.append(current_chocolate)
print("Great! You made all the chocolate milkshakes needed!" if milkshakes == 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join([str(x) for x in chocolates]) if chocolates else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in milk]) if milk else 'empty'}")
