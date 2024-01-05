from collections import deque


code_time = deque([int(x) for x in input().split()])
tasks_count = deque([int(x) for x in input().split()])

ducks_count = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while code_time and tasks_count:
    programmer_time = code_time.popleft()
    tasks = tasks_count.pop()

    time = programmer_time * tasks

    if time > 240:
        code_time.append(programmer_time)
        tasks_count.append(tasks - 2)

    else:
        if 180 < time:
            ducks_count["Small Yellow Rubber Ducky"] += 1
        elif 120 < time:
            ducks_count["Big Blue Rubber Ducky"] += 1
        elif 60 < time:
            ducks_count["Thor Ducky"] += 1
        elif 0 < time:
            ducks_count["Darth Vader Ducky"] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in ducks_count.items():
    print(f"{duck}: {count}")
