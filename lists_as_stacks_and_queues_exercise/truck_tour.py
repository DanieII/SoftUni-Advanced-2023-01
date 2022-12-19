from collections import deque

number_of_stations = int(input())
queue = deque()
for _ in range(number_of_stations):
    split = input().split()
    queue.append([int(split[0]), int(split[1])])

for number_of_station in range(number_of_stations):
    fuel_tank = 0
    completed_stations = 0
    for station in queue:
        amount = station[0]
        distance = station[1]
        fuel_tank += amount
        if distance > fuel_tank:
            break
        fuel_tank -= distance
        completed_stations += 1
    if completed_stations == number_of_stations:
        print(number_of_station)
        break
    queue.rotate(-1)
