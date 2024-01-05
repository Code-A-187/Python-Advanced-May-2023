size = int(input())

battlefield = []
mines_hit = 0
ships_hit = 0
submarine_pos =[]
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(size):
    battlefield.append([x for x in input()])

    if 'S' in battlefield[row]:
        submarine_pos = [row, battlefield[row].index('S')]
        battlefield[row][submarine_pos[1]] = "-"


while True:
    direction = input()
    submarine_pos = [submarine_pos[0] + directions[direction][0], submarine_pos[1] + directions[direction][1]]
    if battlefield[submarine_pos[0]][submarine_pos[1]] == '-':
        continue
    elif battlefield[submarine_pos[0]][submarine_pos[1]] == 'C':
        ships_hit += 1
        if ships_hit == 3:
            battlefield[submarine_pos[0]][submarine_pos[1]] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    elif battlefield[submarine_pos[0]][submarine_pos[1]] == '*':
        mines_hit += 1
        if mines_hit > 2:
            battlefield[submarine_pos[0]][submarine_pos[1]] = 'S'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_pos[0]}, {submarine_pos[1]}]!")
            break
    battlefield[submarine_pos[0]][submarine_pos[1]] = '-'

for i in battlefield:
    print(''.join(map(str, i)))
