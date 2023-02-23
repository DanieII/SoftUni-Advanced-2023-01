number_of_names = int(input())
all_names = [input() for _ in range(number_of_names)]
unique_names = set(all_names)
[print(x) for x in unique_names]
