number_of_names = int(input())
odd = set()
even = set()

for r in range(1, number_of_names + 1):
    current_name = list(input())
    ascii_sum = sum([ord(x) for x in current_name])
    final_value = ascii_sum // r
    if final_value % 2 == 0:
        even.add(final_value)
    else:
        odd.add(final_value)
odd_sum = sum(odd)
even_sum = sum(even)
if odd_sum == even_sum:
    print(*odd.union(even), sep=", ")
elif odd_sum > even_sum:
    print(*odd.difference(even), sep=", ")
elif even_sum > odd_sum:
    print(*odd.symmetric_difference(even), sep=", ")
