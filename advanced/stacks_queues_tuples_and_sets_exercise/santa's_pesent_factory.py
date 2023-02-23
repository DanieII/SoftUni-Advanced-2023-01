from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

needed = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted = []
while materials and magic_values:
    current_material = materials.pop()
    current_magic = magic_values.popleft()
    product = current_material * current_magic

    if needed.get(product):
        crafted.append(needed[product])
    else:
        if product < 0:
            new = current_magic + current_material
            materials.append(new)
        elif product > 0:
            materials.append(current_material + 15)
        else:
            if current_material != 0:
                materials.append(current_material)
            elif current_magic != 0:
                magic_values.appendleft(current_magic)

if {"Doll", "Wooden train"}.issubset(set(crafted)) or {"Teddy bear", "Bicycle"}.issubset(set(crafted)):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for present in sorted(set(crafted)):
    print(f"{present}: {crafted.count(present)}")
