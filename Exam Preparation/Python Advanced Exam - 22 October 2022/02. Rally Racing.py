size = int(input())
car_number = input()
covered_distance = 0
road = []
current_position = [0, 0]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    road.append(input().split())

while True:
    command = input()
    if command == 'End':
        print(f"Racing car {car_number} DNF.")
        road[current_position[0]][current_position[1]] = "C"
        break
    else:
        r = current_position[0] + directions[command][0]
        c = current_position[1] + directions[command][1]
        current_position = [r, c]
        if road[r][c] == ".":
            covered_distance += 10
        elif road[r][c] == "T":
            road[r][c] = '.'
            for row in range(size):
                for col in range(size):
                    if road[row][col] == 'T':
                        road[row][col] = '.'
                        current_position = [row, col]
            covered_distance += 30
        elif road[r][c] == "F":
           print(f"Racing car {car_number} finished the stage!")
           covered_distance += 10
           road[current_position[0]][current_position[1]] = "C"
           break

print(f"Distance covered {covered_distance} km.")
for i in road:
    print(''.join(map(str, i)))
