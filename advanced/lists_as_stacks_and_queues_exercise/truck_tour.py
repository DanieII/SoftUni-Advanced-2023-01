from collections import deque

number_of_stations = int(input())
petrol_pumps = deque([int(x) for x in input().split()] for i in range(number_of_stations))

for index in range(number_of_stations):
    fuel = 0
    completed_stations = 0
    current_circle = petrol_pumps.copy()
    for _ in range(number_of_stations):
        petrol, to_next = current_circle[0]
        current_circle.rotate(-1)
        fuel += petrol
        if fuel - to_next < 0:
            break
        fuel -= to_next
        completed_stations += 1

    if completed_stations == number_of_stations:
        print(index)
        break
    petrol_pumps.rotate(-1)

# Old solution
# number_of_stations = int(input())
# queue = deque()
# for _ in range(number_of_stations):
#     split = input().split()
#     queue.append([int(split[0]), int(split[1])])
#
# for number_of_station in range(number_of_stations):
#     fuel_tank = 0
#     completed_stations = 0
#     for station in queue:
#         amount = station[0]
#         distance = station[1]
#         fuel_tank += amount
#         if distance > fuel_tank:
#             break
#         fuel_tank -= distance
#         completed_stations += 1
#     if completed_stations == number_of_stations:
#         print(number_of_station)
#         break
#     queue.rotate(-1)
