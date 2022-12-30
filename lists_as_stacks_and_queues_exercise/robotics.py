from collections import deque
from datetime import datetime, timedelta


def increase_the_seconds():
    for index in range(len(robots)):
        if robots[index][2] == "BUSY":
            robots[index][3] += 1
            if robots[index][3] == robots[index][1]:
                robots[index][2] = "FREE"
                robots[index][3] = 0


def start_working(current_time):
    r[2] = "BUSY"
    products.popleft()
    time = datetime.strftime(current_time, "%H:%M:%S")
    return time


robots = []
for robot in input().split(";"):
    name, time_as_str = robot.split("-")
    time = int(time_as_str)
    robots.append([name, time, "FREE", 0])
time = datetime.strptime(input(), "%H:%M:%S") + timedelta(seconds=1)
products = deque([input()])
while True:
    command = input()
    if command == "End":
        break
    products.append(command)

while products:
    completed = False
    current_product = products[0]
    increase_the_seconds()
    for r in robots:
        current_robot = r[0]
        current_runtime = r[1]
        current_state = r[2]
        if current_state == "FREE":
            current_time = start_working(time)
            print(f"{current_robot} - {current_product} [{current_time}]")
            completed = True
            break
    time += timedelta(seconds=1)
    if not completed:
        products.append(products.popleft())
