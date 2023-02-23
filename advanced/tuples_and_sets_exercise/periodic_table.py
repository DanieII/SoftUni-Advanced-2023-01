lines = int(input())
elements = set()
for _ in range(lines):
    all_elements = input().split()
    for el in all_elements:
        elements.add(el)
print(*elements, sep="\n")
