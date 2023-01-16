lines = int(input())
longest = set()

for _ in range(lines):
    first_values, second_values = [[int(el) for el in i.split(",")] for i in input().split("-")]

    first_range = set(range(first_values[0], first_values[1] + 1))
    second_range = set(range(second_values[0], second_values[1] + 1))

    intersection = first_range.intersection(second_range)
    if len(intersection) > len(longest):
        longest = intersection
print(f"Longest intersection is {list(longest)} with length {len(longest)}")

# Old solution
# lines = int(input())
# longest = None
# largest_length = 0
#
# for _ in range(lines):
#     first, second = input().split("-")
#
#     first_start, first_end = [int(x) for x in first.split(",")]
#     second_start, second_end = [int(x) for x in second.split(",")]
#     first_numbers = set(x for x in range(first_start, first_end + 1))
#     second_numbers = set(x for x in range(second_start, second_end + 1))
#     intersection = first_numbers.intersection(second_numbers)
#     if not longest:
#         longest = f"Longest intersection is {list(intersection)} with length {len(intersection)}"
#         largest_length = len(intersection)
#         continue
#     if len(intersection) > largest_length:
#         longest = f"Longest intersection is {list(intersection)} with length {len(intersection)}"
#         largest_length = len(intersection)
# print(longest)
