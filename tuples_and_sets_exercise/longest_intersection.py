lines = int(input())
longest = None
largest_length = 0

for _ in range(lines):
    first, second = input().split("-")

    first_start, first_end = [int(x) for x in first.split(",")]
    second_start, second_end = [int(x) for x in second.split(",")]
    first_numbers = set(x for x in range(first_start, first_end + 1))
    second_numbers = set(x for x in range(second_start, second_end + 1))
    intersection = first_numbers.intersection(second_numbers)
    if not longest:
        longest = f"Longest intersection is {list(intersection)} with length {len(intersection)}"
        largest_length = len(intersection)
        continue
    if len(intersection) > largest_length:
        longest = f"Longest intersection is {list(intersection)} with length {len(intersection)}"
        largest_length = len(intersection)
print(longest)
