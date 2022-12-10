lst = input().split()
number_of_toss = int(input())
last_index = 0
difference = number_of_toss
while len(lst) > 1:
    while difference > len(lst):
        difference -= len(lst[last_index:])
        last_index = 0
    current_name = lst[last_index + difference - 1]
    last_index = lst.index(current_name)
    lst.remove(current_name)
    print(f"Removed {current_name}")
    difference = number_of_toss
print(f"Last is {lst[0]}")
