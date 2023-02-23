jobs = [int(x) for x in input().split(", ")]
interested = int(input())

cycle = 0
while True:
    current_index = jobs.index(min([x for x in jobs if x]))
    shortest = jobs[current_index]

    # Change the value to None so the indexes don't change
    jobs[current_index] = None
    cycle += shortest

    if current_index == interested:
        break

print(cycle)
