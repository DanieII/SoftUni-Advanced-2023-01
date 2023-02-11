from collections import deque

orders = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]


def make_pizza(needed, capacity):
    global pizzas_made
    result = needed - capacity
    if capacity > needed:
        pizzas_made += needed
    else:
        pizzas_made += capacity
    return result


pizzas_made = 0
while orders and employees:
    current_order = orders.popleft()
    current_employee = employees.pop()

    if current_order <= 0 or current_order > 10:
        employees.append(current_employee)
        continue
    result = make_pizza(current_order, current_employee)
    if result > 0:
        orders.appendleft(result)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")
