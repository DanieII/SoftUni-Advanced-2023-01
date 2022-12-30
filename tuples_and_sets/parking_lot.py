parking = set()
number_of_cars = int(input())
for _ in range(number_of_cars):
    command, plate = input().split(", ")
    if command == "IN":
        parking.update([plate])
    elif command == "OUT":
        parking.remove(plate)
if parking:
    [print(x) for x in parking]
else:
    print("Parking Lot is Empty")
