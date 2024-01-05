from collections import deque

caffeineInDrink = list([int(x) for x in input().split(', ')])
drinks = deque([int(x) for x in input().split(', ')])
caffeine_sum = 0

while caffeineInDrink and drinks:
    caffeine = caffeineInDrink.pop()
    drink = drinks.popleft()
    multiply = caffeine * drink

    if caffeine_sum + multiply <= 300:
        caffeine_sum += multiply
    else:
        drinks.append(drink)

        if caffeine_sum - 30 < 0:
            caffeine_sum = 0
        else:
            caffeine_sum -= 30

if drinks:
    print(f"Drinks left: {', '.join(map(str, drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {caffeine_sum} mg caffeine.')
