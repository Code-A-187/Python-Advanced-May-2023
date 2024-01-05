from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = list(map(int, input().split()))

items_count = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while True:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    if not medicaments:
        print("Medicaments are empty.")
        break
    textile = textiles.popleft()
    medicament = medicaments.pop()
    sum_ = textile + medicament
    if sum_ == 30:
        items_count["Patch"] += 1
    elif sum_ == 40:
        items_count["Bandage"] += 1
    elif sum_ == 100:
        items_count["MedKit"] += 1
    elif sum_ > 100:
        items_count["MedKit"] += 1
        sum_ -= 100
        medicaments[-1] += sum_
    else:
        medicaments.append(medicament + 10)

for name, count in sorted(items_count.items(), key=lambda x: (-x[1],x[0])):
    if int(count) > 0:
        print(f"{name} - {count}")

if medicaments:
    print(f"Medicaments left: {', '.join((str(x) for x in sorted(medicaments, reverse= True)))}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in sorted(textiles, reverse= True))}")
