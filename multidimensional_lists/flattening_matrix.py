rows = int(input())
lst = []
for i in range(rows):
    lst.extend([int(x) for x in input().split(", ")])
print(lst)
