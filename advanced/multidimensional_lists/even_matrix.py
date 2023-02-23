number_of_nested_lists = int(input())
matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(number_of_nested_lists)]
print(matrix)
