from collections import deque

quantity_of_food = int(input())
orders = deque(int(x) for x in input().split())
biggest_order = max(orders)
print(biggest_order)
completed = True
for _ in range(len(orders)):
    order = orders.popleft()
    if quantity_of_food - order >= 0:
        quantity_of_food -= order
    else:
        # Putting the order back in the queue because it gets removed first
        orders.appendleft(order)
        completed = False
        break

if completed:
    print("Orders complete")
else:
    left = " ".join([str(x) for x in orders])
    print(f"Orders left: {left}")
