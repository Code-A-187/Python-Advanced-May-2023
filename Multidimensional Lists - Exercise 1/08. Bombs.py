matrix = []

for _ in range(int(input())):
    matrix.append([int(x) for x in input().split()])

info = input().split()


for el in info:
    x, y = [int(num) for num in el.split(',')]
    damage = matrix[x][y]
    for row in range(x - 1, x + 2):
        for col in range(y - 1, y + 2):
            if col < 0 or row < 0 or row > len(matrix) - 1 or col > len(matrix) - 1:
                continue
            elif matrix[row][col] <= 0:
                continue
            elif matrix[row][col] == matrix[x][y]:
                matrix[row][col] = 0
            else:
                matrix[row][col] -= damage

alive_cells = 0
sum_of_cells = 0
for el in matrix:
    for num in el:
        if num > 0:
            alive_cells += 1
            sum_of_cells += num
print(f"Alive cells: {alive_cells}\nSum: {sum_of_cells}")
for el in matrix:
    print(' '.join(map(str, el)))
