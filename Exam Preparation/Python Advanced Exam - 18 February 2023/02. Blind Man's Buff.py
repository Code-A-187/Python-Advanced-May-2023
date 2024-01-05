rows, cols = input().split()

matrix = []
player_position = []
touches_count = 0
moves_count = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(int(rows)):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        player_position = [row, matrix[row].index('B')]
        matrix[row][player_position[1]] = "-"



while True:
    direction = input()
    if direction == 'Finish':
        break

    check = [player_position[0] + directions[direction][0], player_position[1] + directions[direction][1]]

    if not (0 <= check[0] < int(rows) and 0 <=  check[1] < int(cols)):
            continue
    elif matrix[check[0]][check[1]] == 'O':
            continue
    elif matrix[check[0]][check[1]] == 'P':
        player_position = check
        moves_count += 1
        touches_count += 1
        matrix[check[0]][check[1]] = '-'
        if touches_count == 3:
            break
    elif matrix[check[0]][check[1]] == '-':
        player_position = check
        moves_count += 1

print(f"Game over!\nTouched opponents: {touches_count} Moves made: {moves_count}")
