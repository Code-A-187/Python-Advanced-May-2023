rows = int(input())
commands = input().split()
mine = [input().split() for _ in range(rows)]

coals = 0
mined_coals = 0
miner_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    if "s" in mine[row]:
        miner_position = [row, mine[row].index('s')]
    if 'c' in mine[row]:
        coals += mine[row].count('c')

for command in commands:
    if 0 <= miner_position[0] + directions[command][0] < rows and \
            0 <= miner_position[1] + directions[command][1] < rows:
        miner_position = [
            miner_position[0] + directions[command][0],
            miner_position[1] + directions[command][1],
        ]
        if mine[miner_position[0]][miner_position[1]] == 'e':
            print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
            break

        elif mine[miner_position[0]][miner_position[1]] == 'c':
            mine[miner_position[0]][miner_position[1]] = '*'
            mined_coals += 1
            if mined_coals == coals:
                print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
                break
    else:
        continue
else:
    print(f"{coals - mined_coals} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
