from collections import deque

green_sec = int(input())
free_window = int(input())

lane_of_cars = deque()
passed_cars = 0

info = input()

while info != "END":
    if info != "green":
        lane_of_cars.append(info)
    else:
        current_green = green_sec
        while current_green > 0 and lane_of_cars:
            car = lane_of_cars.popleft()
            time = current_green + free_window

            if len(car) > time:
                print(f"A crash happened! \n {car} was hit at {car[time]}.")
                raise SystemExit
            else:
                current_green -= len(car)
                passed_cars += 1

    info = input()

print(f"Everyone is safe.\n{passed_cars} total cars passed the crossroads.")
