clothes = [int(x) for x in input().split()]
capacity = int(input())
used_racks = 0
rack = []
for index in range(len(clothes) - 1, -1, -1):
    check = False
    current_number = clothes.pop()
    rack.append(current_number)
    if sum(rack) == capacity:
        if clothes:
            used_racks += 1
            rack.clear()
            check = True
    elif sum(rack) > capacity:
        used_racks += 1
        rack = [current_number]
    if index == 0 and not check:
        # If it's the last item and the current sum is less than the capacity, use one last rack
        used_racks += 1
print(used_racks)
