clothes = [int(x) for x in input().split()]
capacity = int(input())
current_rack = 1
current_space = capacity

while clothes:
    current_cloth = clothes.pop()

    if current_space - current_cloth >= 0:
        current_space -= current_cloth
        continue

    current_rack += 1
    current_space = capacity - current_cloth

print(current_rack)

# Old solution
# clothes = [int(x) for x in input().split()]
# capacity = int(input())
# used_racks = 0
# rack = []
# for index in range(len(clothes) - 1, -1, -1):
#     check = False
#     current_number = clothes.pop()
#     rack.append(current_number)
#     if sum(rack) == capacity:
#         if clothes:
#             used_racks += 1
#             rack.clear()
#             check = True
#     elif sum(rack) > capacity:
#         used_racks += 1
#         rack = [current_number]
#     if index == 0 and not check:
#         # If it's the last item and the current sum is less than the capacity, use one last rack
#         used_racks += 1
# print(used_racks)
