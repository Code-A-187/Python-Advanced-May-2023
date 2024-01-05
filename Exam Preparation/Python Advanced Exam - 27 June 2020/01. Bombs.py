from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = list([int(x) for x in input().split(', ')])
bombs_made =0
bombs_dict ={
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_effects and bomb_casings:
    if bombs_dict["Cherry Bombs"] >= 3 and bombs_dict["Datura Bombs"] >= 3 and bombs_dict["Smoke Decoy Bombs"] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break

    effect = bomb_effects.popleft()
    sum_ = effect + bomb_casings[-1]

    if sum_ == 40:
        bombs_dict["Datura Bombs"] += 1
        bomb_casings.pop()
    elif sum_ == 60:
        bombs_dict["Cherry Bombs"] += 1
        bomb_casings.pop()
    elif  sum_ == 120:
        bombs_dict["Smoke Decoy Bombs"] += 1
        bomb_casings.pop()
    else:
        bomb_effects.appendleft(effect)
        bomb_casings[-1] -= 5

else:
    print(f"You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print("Bomb Casings: empty")
for i in bombs_dict:
    print(f"{i}: {bombs_dict[i]}")
