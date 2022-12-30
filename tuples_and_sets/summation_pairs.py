numbers = [int(x) for x in input().split()]
target = int(input())
used_nums = set()
for first_index in range(len(numbers)):
    first_num = numbers[first_index]

    current_num_index = first_index
    if current_num_index not in range(len(numbers)):
        current_num_index = 0

    for second_num in numbers[:current_num_index] + numbers[current_num_index + 1:]:
        if first_num + second_num == target and first_num not in used_nums:
            print(f"{first_num} + {second_num} = {target}")
            used_nums.add(second_num)
    used_nums.add(first_num)
