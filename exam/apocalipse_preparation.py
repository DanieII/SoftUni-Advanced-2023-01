from collections import deque

textile = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

items = {
    "Patch": lambda x: x == 30,
    "Bandage": lambda x: x == 40,
    "MedKit": lambda x: x == 100,
}

created = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textile and medicaments:
    current_textile = textile.popleft()
    current_medicament = medicaments.pop()
    result = current_textile + current_medicament

    for item, needed in items.items():
        if needed(result):
            created[item] += 1
            break
    else:
        if result > 100:
            created["MedKit"] += 1
            remaining = result - 100
            medicaments.append(medicaments.pop() + remaining)
            continue
        else:
            medicaments.append(current_medicament + 10)

if not textile and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textile:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

created_result = [x for x in created.values() if x]
if created_result:
    only_with_created = {k: v for k, v in created.items() if v}
    sorted_created = dict(sorted(only_with_created.items(), key=lambda x: (-x[1], x[0])))
    for k, v in sorted_created.items():
        print(f"{k} - {v}")

if medicaments:
    medicaments = medicaments[::-1]
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments])}")
if textile:
    print(f"Textiles left: {', '.join([str(x) for x in textile])}")
