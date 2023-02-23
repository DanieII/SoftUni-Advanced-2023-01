from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts = {
    "Gemstone": lambda x: 100 <= x <= 199,
    "Porcelain Sculpture": lambda x: 200 <= x <= 299,
    "Gold": lambda x: 300 <= x <= 399,
    "Diamond Jewellery": lambda x: 400 <= x <= 499,
}

made = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}


def check_for_available(value):
    for k, v in gifts.items():
        if v(value):
            made[k] += 1
            return True
    return False


def check_for_success():
    if (made["Gemstone"] and made["Porcelain Sculpture"]) or (made["Gold"] and made["Diamond Jewellery"]):
        return True
    return False


while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()
    result = current_material + current_magic_level

    if not check_for_available(result):
        if result < 100:
            if result % 2 == 0:
                result = 2 * current_material + 3 * current_magic_level
            else:
                result *= 2
        elif result > 499:
            result /= 2

        if result > 100:
            check_for_available(result)

print("The wedding presents are made!" if check_for_success() else "Aladdin does not have enough wedding presents.")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

made = {k: v for k, v in made.items() if v}
for k, v in sorted(made.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")
