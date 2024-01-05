size = int(input())

field = []
snake_pos = []
food_quantity = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append([x for x in input()])

    if 'S' in field[row]:
        snake_pos = [row, field[row].index('S')]
        field[row][snake_pos[1]] = "."

while True:
    direction = input()
    snake_pos = [snake_pos[0] + directions[direction][0], snake_pos[1] + directions[direction][1]]

    if not (0 <= snake_pos[0] < size and 0 <=  snake_pos[1] < size):
        print("Game over!")
        break
    elif field[snake_pos[0]][snake_pos[1]] == "*":
        food_quantity += 1
        field[snake_pos[0]][snake_pos[1]] = '.'
        if food_quantity == 10:
            field[snake_pos[0]][snake_pos[1]] = 'S'
            print('You won! You fed the snake.')
            break
    elif field[snake_pos[0]][snake_pos[1]] == "B":
        field[snake_pos[0]][snake_pos[1]] = '.'
        for row in range(size):
            for col in range(size):
                if field[row][col] == 'B':
                    field[row][col] = '.'
                    snake_pos = [row, col]
    elif field[snake_pos[0]][snake_pos[1]] == "-":
        field[snake_pos[0]][snake_pos[1]] = '.'

print(f"Food eaten: {food_quantity}")
for i in field:
    print(''.join(map(str, i)))
