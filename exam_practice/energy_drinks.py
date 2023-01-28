from collections import deque

MAX_CAFFEINE = 300
consumed = 0
caffeine = [int(x) for x in input().split(", ")]
drinks = deque(int(x) for x in input().split(", "))
while caffeine and drinks:
    current_caffeine = caffeine.pop()
    current_drink = drinks.popleft()
    result = current_drink * current_caffeine
    if consumed + result <= MAX_CAFFEINE:
        consumed += result
    else:
        drinks.append(current_drink)
        if consumed - 30 > 0:
            consumed -= 30
        else:
            consumed = 0
if drinks:
    print(f"Drinks left: {', '.join([str(x) for x in drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {consumed} mg caffeine.")
