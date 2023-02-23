from collections import deque

seats = [[int(x[:-1]), x[-1]] for x in input().split(", ")]
first_sequence = deque(int(x) for x in input().split(", "))
second_sequence = deque(int(x) for x in input().split(", "))

matched_seats = []
matched = 0
rotations = 0
while True:
    current_first = first_sequence.popleft()
    current_second = second_sequence.pop()

    character = chr(current_first + current_second)
    found = False
    remove_both = False

    rotations += 1

    for num, letter in seats:
        if letter == character:
            if [letter, current_first] in matched_seats or [letter, current_second] in matched_seats:
                remove_both = True
                break
            if num == current_first or num == current_second:
                matched += 1
                matched_seats.append([letter, num])
                found = True
                break

    if rotations == 10 or matched == 3:
        break

    if not found and not remove_both:
        first_sequence.append(current_first)
        second_sequence.appendleft(current_second)

print(f"Seat matches: {', '.join(''.join([str(i) for i in x[::-1]]) for x in matched_seats)}")
print(f"Rotations count: {rotations}")
