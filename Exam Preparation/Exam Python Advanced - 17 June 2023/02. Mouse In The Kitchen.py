row, col = [int(x) for x in input().split(',')]

matrix = []
cheese_count = 0
mouse_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(row):
    matrix.append([x for x in input()])

    if "M" in matrix[row]:
        mouse_pos = [row, matrix[row].index("M")]
        matrix[row][mouse_pos[1]] = "*"

    if "C" in matrix[row]:
        cheese_count += matrix[row].count("C")

while True:
    direction = input()
    if direction == "danger":
        print("Mouse will come back later!")
        break

    r, c = mouse_pos[0] + directions[direction][0], mouse_pos[1] + directions[direction][1]

    if not (0 <= r < row and 0 <=  c < col):
        print("No more cheese for tonight!")
        break
    if matrix[r][c] == '@':
        continue

    mouse_pos = [r, c]

    if matrix[mouse_pos[0]][mouse_pos[1]] == 'C':
        cheese_count -= 1
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
        matrix[r][c] = '*'

    elif matrix[mouse_pos[0]][mouse_pos[1]] == 'T':
        print("Mouse is trapped!")
        break

matrix[mouse_pos[0]][mouse_pos[1]] = 'M'

for i in matrix:
    print(''.join(map(str, i)))
