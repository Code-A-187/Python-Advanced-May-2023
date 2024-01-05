rows = int(input())

field = [list(input().split())for _ in range(rows)]
bunny_position = []
best_direction = None
best_path = []
max_eggs = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    if "B" in field[row]:
        bunny_position = [row, field[row].index('B')]


for direction, position in directions.items():
    row, col = [
        bunny_position[0] + position[0],
        bunny_position[1] + position[1],
    ]
    path = []
    egg_counter = 0

    while 0 <= row < rows and 0 <= col < rows:
        if field[row][col] == 'X':
            break

        egg_counter += int(field[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if egg_counter >= max_eggs:
        max_eggs = egg_counter
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs)
