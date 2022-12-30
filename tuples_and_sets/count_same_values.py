numbers = (float(x) for x in input().split())
my_dict = {}
for number in numbers:
    if number not in my_dict:
        my_dict[number] = 0
    my_dict[number] += 1
[print(f"{x} - {my_dict[x]} times") for x in my_dict]
