from collections import deque

cars = deque()
green_light = int(input())
free_window = int(input())
total_cars = 0

while True:
    command = input()
    if command == "END":
        break

    if command != "green":
        cars.append(command)
        continue

    current_green = green_light
    while current_green > 0 and cars:
        current_car = cars.popleft()
        available_time = current_green + free_window
        if len(current_car) > available_time:
            last_character = current_car[available_time]
            print(f"A crash happened!\n{current_car} was hit at {last_character}.")
            quit()
        current_green -= len(current_car)
        total_cars += 1

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")

# Old solution
# def pass_func():
#     global cars_passed, current_green_light_time, over
#     cars_passed += 1
#     current_green_light_time -= characters
#     if current_green_light_time <= 0:
#         over = True
#
#
# green_light_time = int(input())
# free_window_time = int(input())
# cars = deque([])
# cars_passed = 0
# command = input()
#
# while True:
#     if command == "END":
#         break
#
#     if command != "green":
#         cars.append(command)
#     else:
#         over = False
#         current_green_light_time = green_light_time
#         for _ in range(len(cars)):
#             car = cars.popleft()
#             characters = len(car)
#             if characters > current_green_light_time + free_window_time:
#                 last_character = car[current_green_light_time + free_window_time]
#                 print("A crash happened!")
#                 print(f"{car} was hit at {last_character}.")
#                 quit()
#
#             pass_func()
#             if over:
#                 break
#     command = input()
# print("Everyone is safe.")
# print(f"{cars_passed} total cars passed the crossroads.")
