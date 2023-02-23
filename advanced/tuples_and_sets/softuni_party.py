number_of_guests = int(input())
all_reservations = {input() for _ in range(number_of_guests)}
who_came = set()
while True:
    command = input()
    if command == "END":
        break
    who_came.add(command)

missing_guests = {
    "VIP": [x for x in list(all_reservations) if x not in who_came and x[0].isdigit()],
    "NORMAL": [x for x in list(all_reservations) if x not in who_came and not x[0].isdigit()]}
missing_guests["VIP"].sort(key=lambda x: x)
missing_guests["NORMAL"].sort(key=lambda x: x)


print(len(missing_guests["VIP"]) + len(missing_guests["NORMAL"]))
[print(x) for x in missing_guests["VIP"]]
[print(x) for x in missing_guests["NORMAL"]]
