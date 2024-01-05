size = int(input())
moves = (x for x in input().split(", "))
matrix = []
squirrel_pos = []
hazelnuts_count = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append([x for x in input()])

    if 's' in matrix[row]:
        squirrel_pos = [row, matrix[row].index('s')]
        matrix[row][squirrel_pos[1]] = "*"

for direction in moves:
    r = squirrel_pos[0] + directions[direction][0]
    c = squirrel_pos[1] + directions[direction][1]
    squirrel_pos = [r, c]
    if not (0 <= r < len(matrix) and 0 <= c < len(matrix)):
        print("The squirrel is out of the field.")
        break
    elif matrix[r][c] == "*":
        continue
    elif matrix[r][c] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    else:
        hazelnuts_count += 1
        if hazelnuts_count == 3:
            print("Good job! You have collected all hazelnuts!")
            break
    matrix[r][c] = '*'
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_count}")
